; ControlFocus("title", "text", "ClassnameNN") ControlFocus�������÷�
ControlFocus("��", "", "Edit1")
; �ȴ�10��
 WinWait("[CLASS:#32770]", "", 10)
; ���ļ����ؼ�������Ҫ�ϴ����ļ�ȫ·��
 ControlSetText("��", "", "Edit1", "D:\test_upload_file.txt")

 Sleep(2000)
; ����򿪰�ť
 ControlClick("��", "", "Button1")