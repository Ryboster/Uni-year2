### **Date: Thu 28 Aug 2025**<br>

# Activities

* 1pm - Got to work on ticket

* 2:15pm - Wrote a script for automatically opening the most recent daily log<br>

* 2:30pm - Researched how to make the script executable<br>

* 2:40pm - Researched Linux Desktop Entries<br>

* 2:55pm - Created a new desktop entry and made it executable - it works! <br>

* 3pm - Made another script for opening this year's directory and made a .desktop file for it.<br>

* 3:10pm - Moved both .desktop files to ~/.local/share/applications and saved them on sidebar.<br>

* 3:20pm - Fetched quick icons for the new applications.<br><br>

* 3:35pm - Break.<br>

* 4:10pm - back to work on the ticket

* 5:05pm - After a long time of seeking, I finally found the problematic line and replaced the usage of previously instantiated thisItemPrefab variable (which was lossful) with Resources.Load<>() (which is lossless).

* 5:10pm - Took another ticket. The task is to make it so that every wheat crop has 10-15 plants instead of just one.

* 5:20pm - Created another two quick applications. One for opening my Scattered-Lands directory, and another for copying my token without revealing it.

* 7pm - Back to work on the ticket. Upon the first implementation, I discovered a problem with the performance. The number of wheat plants scales very poorly.

* 7:20pm - Did further bugfixing to better identify the issue.

* 7:30pm - Removed colliders to see if it's the close proximity of colliders and rigidbodies that's causing the lag. Upon removal, problem persists.

* 8:10pm - Replaced the wheat prefab with another prefab. The drop is performance using other prefabs (tomato) is a lot less.

* 8:30pm - Need a break from the problem. Got to work on improving my applications. The aim is to assign/group window pop ups to/with the application icons on sidebars.

* 8:50pm - Read up on WM classes. Ran the Xprop example to find out the class unity runs in.

* 9:30pm - Ran into issues with grouping my `OpenSL.desktop` file with gedit. Downloaded MarkText to try with it instead.

* 10pm - Tried couple different MarkTexts - .AppImage, .desktop, snap version. Same problem across them all. Despite the `WM_CLASS` clearly matching, the document kept starting in an independent window.

* 10:40pm - Got it! Changed filename of `OpenLog.desktop` to `marktext.desktop`. This finally worked.

* 10:50pm - Got to work on making my `OpenSLTerminal.desktop` entry independent.

* 11:10pm - Found out about `--class=<classname>` in `gnome-bash` command. Set a custom flag and matched it in my desktop entry. voila!

* 11:30pm - Gpt says nautilus also accepts the `--class` flag. Tried making my `OpenYear.desktop` independent too.

# Issues/Errors

<br>

# Next Steps

<br>

## Resources

* [directory - folders in sidebar - Ask Ubuntu](https://askubuntu.com/questions/1414795/folders-in-sidebar)

* [Guide to Desktop Entry Files in Linux | Baeldung on Linux](https://www.baeldung.com/linux/desktop-entry-files)

* [ubuntu - Quickly create an entry in the side bar Launcher - Super User](https://superuser.com/questions/552959/quickly-create-an-entry-in-the-side-bar-launcher)

* [Creating Linux Desktop Shortcuts | RichHewlett.com](https://richhewlett.com/2021/03/27/creating-linux-desktop-shortcuts/)

* https://forums.linuxmint.com/viewtopic.php?t=387565

* [i3 - How to define wm class for terminal commands in .desktop files - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/574814/how-to-define-wm-class-for-terminal-commands-in-desktop-files)

* [unity - Creating a .desktop file for a new application - Ask Ubuntu](https://askubuntu.com/questions/281293/creating-a-desktop-file-for-a-new-application)

* [What does the StartupWMClass field of a .desktop file represent? - Ask Ubuntu](https://askubuntu.com/questions/367396/what-does-the-startupwmclass-field-of-a-desktop-file-represent)

* [bash - What is the meaning of &amp; at the end of a command? - Ask Ubuntu](https://askubuntu.com/questions/1107124/what-is-the-meaning-of-at-the-end-of-a-command)

#### xprop example

```bash
xprop | grep WM_CLASS
```

#### OpenLog.desktop:

```bash
[Desktop Entry]
Name=OpenLog
Exec=/home/snek/applications/open_daylog.sh
Icon=/home/snek/Pictures/icons/openlog.svg
Type=Application
StartupWMClass=marktext
Terminal=false
StartupNotify=true
Categories=Development;
```

#### OpenYear.desktop:

```bash
[Desktop Entry]
Type=Application
Name=OpenYear
Exec=nautilus /home/snek/Desktop/portfolio/year-2-1
Icon=/home/snek/Pictures/icons/openyear.png
Terminal=false
StartupNotify=true
Categories=Utility;
```

#### OpenSL.desktop

```bash
[Desktop Entry]
Name=OpenSL
Exec=/home/snek/Unity/Hub/Editor/6000.2.0b11/Editor/Unity -projectPath /home/snek/Desktop/portfolio/Scattered-Lands >/dev/null 2>&1
Icon=/home/snek/Pictures/icons/OpenSL1.png
Type=Application
Categories=Development;
Terminal=false
StartupNotify=true
StartupWMClass=Unity
```
