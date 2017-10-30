import os,sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR=BASE_DIR+os.sep+'core'

sys.path.append(BASE_DIR)
sys.path.append(CORE_DIR)
import core

core.demo_shoplist.shopping()
