from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

time_format = "%Y%m%d%H%M%S"
cmd = "clickout.bat"


def click():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    keyevent("POWER")
    sleep(1)
    swipe((500, 2000), (500, 0))
    sleep(3)
    start_app("com.sie.mp")
    sleep(3)
    poco("com.sie.mp:id/pllayout").offspring("com.sie.mp:id/drawer_layout").offspring(
        "com.sie.mp:id/ll_title_main").child("android.widget.RelativeLayout")[3].offspring(
        "com.sie.mp:id/img_tab_main_icon").click()
    sleep(3)
    poco("com.sie.mp:id/pllayout").offspring("com.sie.mp:id/drawer_layout").offspring(
        "com.sie.mp:id/viewpager_main_bottom").offspring("com.sie.mp:id/rvData").child(
        "com.sie.mp:id/rl_app_grid_item")[0].offspring("com.sie.mp:id/img_app_grid_item_icon").click()
    sleep(3)
    poco("com.sie.mp:id/attendance_btn").click()
    sleep(3)
    poco("com.sie.mp:id/btn_attendance_submit").click()
    sleep(3)
    keyevent("BACK")
    sleep(1)
    keyevent("BACK")
    sleep(1)
    keyevent("POWER")


def main():
    auto_setup(__file__)
    times = []
    n = int(input("how many times: "))
    for i in range(0, n):
        times.append(time.mktime(time.strptime(input("set %i time: " % i), time_format)))
    now = time.mktime(time.localtime())
    for i in range(0, n):
        print("time %i: %s" % (i, time.strftime(time_format, time.localtime(times[i]))))
        while now < times[i]:
            time.sleep(10)
            now = time.mktime(time.localtime())
            print("now: %s" % time.strftime(time_format, time.localtime()))
        click()


if __name__ == '__main__':
    main()
