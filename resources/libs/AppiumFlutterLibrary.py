
import os
import base64
import robot
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.BuiltIn import RobotNotRunningError
from robot.api import logger
from robot.api.deco import keyword
from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder

class AppiumFlutterLibrary(object):

  def __init__(self):
    self.finder = FlutterFinder()
    self._screenshot_index = 0

  # PUBLIC
  @keyword('Open Application')
  def open_application(self, remote_url, **kwargs):
    desired_caps = kwargs
    self.driver = Remote(str(remote_url), desired_caps)

  @keyword('Click Element')
  def click_element(self, locator: str, strategy: str='value_key'):
    element: FlutterElement = self._get_element(locator, strategy)
    element.click()
    self._html(f'Clicking the element [{locator}]')

  @keyword('Input Text')
  def input_text(self, locator: str, text: str, strategy: str='value_key'):
    element: FlutterElement = self._get_element(locator, strategy)
    element.send_keys(text)
    self._html(f'typing [{text}] in the [{locator}] element')

  @keyword('Get Text')
  def get_text(self, locator: str, strategy: str='value_key'):
    element: FlutterElement = self._get_element(locator, strategy)
    return element.text

  @keyword('Page Back')
  def page_back(self):
    self.finder.page_back()

  @keyword('Clear Text')
  def clear_text(self, locator: str, strategy: str='value_key'):
    element: FlutterElement = self._get_element(locator, strategy)
    self._html(f'clearing text from the [{locator}] element')
    element.clear()

  @keyword('Clear Time Line')
  def clear_time_line(self):
    self.driver.execute('flutter:clearTimeline')

  @keyword('Check Health')
  def check_health(self):
    self.driver.execute('flutter:checkHealth')

  @keyword('Close Application')
  def close_application(self):
    self.driver.close()

  @keyword('Capture Page Screenshot')
  def capture_page_screenshot(self, filename: str=None):
    path, link = self._get_screenshot_paths(filename)
    base = self.driver.get_screenshot_as_base64()
    with open(path, 'wb') as fh:
      fh.write(base64.urlsafe_b64decode(base))
    self._html('</td></tr><tr><td colspan="3"><a href="%s">''<img src="%s" width="800px"></a>' % (link, link))
    

  # @keyword('Get Element Attribute')
  # def get_element_attribute(self, locator: str, attribute: str, strategy: str='value_key'):
  #   element: FlutterElement = self._get_element(locator, strategy)
  #   return element.get_attribute(attribute)

  # @keyword('Wait For Element')
  # def wait_for_element(self, locator: str, timeout: int=100, strategy: str='value_key'):
  #   self.driver.execute('flutter:waitFor', self._get_locator(locator, strategy))

  # @keyword('Wait For Element Absent')
  # def wait_for_element_absent(self, locator: str, strategy: str='value_key'):
  #   self.driver.execute('flutter:waitForAbsent', self._get_locator(locator, strategy))

  # @keyword('Scroll To')
  # def scroll_to(self, locator: str, x: int, y: int, duration: int=200, strategy: str='value_key'):
  #   element: FlutterElement = self._get_element(locator, strategy)
  #   self.driver.execute('flutter:scroll', {
  #     'element': element,
  #     'dx': x,
  #     'dy': y,
  #     'durationMilliseconds': duration,
  #     'frequency': 30
  #   })



  # PRIVATE

  def _get_element(self, locator, strategy='value_key') -> FlutterElement:
    element = self._get_locator(locator, strategy)
    return FlutterElement(self.driver, element)

  def _get_locator(self, locator, strategy='value_key') -> FlutterFinder:
    if strategy == 'value_key':
      return self.finder.by_value_key(locator)
    if strategy == 'text':
      return self.finder.by_text(locator)
    if strategy == 'tooltip':
      return self.finder.by_tooltip(locator)
    if strategy == 'ancestor':
      return self.finder.by_ancestor(locator)
    if strategy == 'descendant':
      return self.finder.by_descendant(locator)
    if strategy == 'semantics':
      return self.finder.by_semantics_label(locator)
    if strategy == 'type':
      return self.finder.by_type(locator)

  # Utilities
  def _html(self, message):
    logger.info(message, True, False)

  def _get_log_dir(self):
    variables = BuiltIn().get_variables()
    logfile = variables['${LOG FILE}']
    if logfile != 'NONE':
      return os.path.dirname(logfile)
    return variables['${OUTPUTDIR}']

  def _get_screenshot_paths(self, filename):
    if not filename:
      self._screenshot_index += 1
      filename = 'appium-screenshot-%d.png' % self._screenshot_index
    else:
      filename = filename.replace('/', os.sep)
    logdir = self._get_log_dir()
    path = os.path.join(logdir, filename)
    link = robot.utils.get_link_path(path, logdir)
    return path, link
  