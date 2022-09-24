from flask import Blueprint
# 实例化蓝本类
main = Blueprint('main', __name__)
# 导入模块与蓝本关联
from . import views, errors
