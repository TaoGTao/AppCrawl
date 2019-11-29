from mitmproxy.tools._main import mitmdump

if __name__ == '__main__':
    from airtest.core.api import *
    # from airtest.core.android.android import Android

    device = connect_device('android:///127.0.0.1:21503?cap_method=javacap')
    print('已安装的应用如下：', device.list_app())
    # device2 = connect_device('android:///127.0.0.1:21513')
    # device1.start_app('com.xingin.xhs')
    # device2.start_app('com.xingin.xhs')
    # print(device2.list_app())


    # from airtest.core.api import *
    # from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    # _device = connect_device('android:///127.0.0.1:21503?cap_method=javacap')
    # start_app('com.xingin.xhs')
    # sleep(20)
    # stop_app('com.xingin.xhs')



    # poco = AndroidUiautomationPoco(device=_device,
    #                                use_airtest_input=True, screenshot_each_action=False)
    # # auto_setup(__file__)
    # poco(text="小红书").click()
    # sleep()
    # poco(name="com.xingin.xhs:id/a3q").click()
    # poco(name="com.xingin.xhs:id/axk").click()
    # poco(name="com.xingin.xhs:id/axk").set_text('迪丽热巴')
    # sleep()
    # poco("com.xingin.xhs:id/bt5").child("android.widget.LinearLayout").offspring("com.xingin.xhs:id/aw9").offspring(
    #     "com.xingin.xhs:id/atp").offspring("com.xingin.xhs:id/eh").child("android.widget.FrameLayout")[0].offspring(
    #     "com.xingin.xhs:id/bx9").click()
    # n = 0
    # while n < 10:
    #     x, y = poco.get_screen_size()
    #     swipe((0.5 * x, 0.8 * y), (0.5 * x, 0.5 * y))
    #     n += 1
    # stop_app()
    #




