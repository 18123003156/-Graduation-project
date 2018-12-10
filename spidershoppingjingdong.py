import requests
from .spidershoppingbase import SpiderShoppingBase
import re
import json
from commonbaby.httpaccess.httpaccess import HttpAccess
from ...clientdatafeedback.profilefeedback import PROFILE
from ...clientdatafeedback.ishoppingorderfeedback import ISHOPPING
from ...clientdatafeedback.profilepicfeedback import PROFILEPIC


class SpiderJingDong(SpiderShoppingBase):

    def __init__(self, task):
        # SpiderMeiTuan.__init__(self,tst:Task, 'meituan', '1000')
        super(SpiderJingDong, self).__init__(task, 'jingdong', 1000)
        self.cookie = self.task.cookie
        self.account = self.task.account