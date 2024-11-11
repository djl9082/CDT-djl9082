Script displays image popup to distract the user. The popup runs every minute and can be closed by pressing the "Escape", "C", or "Tab" keys. 

To run the script, run system.exe in the Downloads folder of the dylan-windowstest box on the CDT-delta openstack project. 

The script can be stopped by ending the task in the task manager. The cat photo is located at "C:/ProgramData/Microsoft/Diagnosis/cat.png" and will break the script if deleted. 

The image is set for 1920x1080 resolution so it will take up the entire screen with a resolution smaller than that.

For comp day, I will get the script on the target machines and and set up a task scheduler so that script runs every 5 minutes if it is stopped by the user. I will also hide it in a more obscure location.
