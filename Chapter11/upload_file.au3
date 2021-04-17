; ControlFocus("title", "text", "ClassnameNN") ControlFocus函数的用法
ControlFocus("打开", "", "Edit1")
; 等待10秒
 WinWait("[CLASS:#32770]", "", 10)
; 在文件名控件里设置要上传的文件全路径
 ControlSetText("打开", "", "Edit1", "D:\test_upload_file.txt")

 Sleep(2000)
; 点击打开按钮
 ControlClick("打开", "", "Button1")