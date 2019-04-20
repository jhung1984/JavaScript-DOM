<!-- 通过sudo dnf install openbox安装openbox，配置文件为/etc/xdg/openbox/menu.xml,也可以通过~/.config/openbox/lxde-rc.xml进行配置 -->
<!-- 也可以通过obconf进行简单配置，安装obconf命令为dnf install obconf -->

    <keybind key="W-C-Down">
      <action name="GrowToEdgeSouth"/>
    </keybind>
    <keybind key="W-C-A-Right">
      <action name="MoveToEdgeEast"/>
    </keybind>
    <keybind key="W-C-A-Left">
      <action name="MoveToEdgeWest"/>
    </keybind>
    <keybind key="W-C-A-Up">
      <action name="MoveToEdgeNorth"/>
    </keybind>
    <keybind key="W-C-A-Down">
      <action name="MoveToEdgeSouth"/>
    </keybind>
    <keybind key="A-Tab">
      <action name="DesktopNext">
      </action>
    </keybind>
    <keybind key="A-S-Tab">
      <action name="SendToDesktopNext">
        <follow>no</follow>
      </action>
    </keybind>
    <keybind key="A-space">
      <action name="ToggleShowDesktop"/>
    </keybind>
    <keybind key="A-Return">
      <action name="ShowMenu">
        <menu>root-menu</menu>
      </action>
    </keybind>
    <keybind key="S-A-Return">
      <action name="ShowMenu">
        <menu>obm-xdg-menu</menu>
      </action>
    </keybind>
    <keybind key="A-F2">
      <action name="Execute">
        <execute>gmrun</execute>
      </action>
    </keybind>
    <keybind key="A-F4">
      <action name="Close"/>
    </keybind>
    <keybind key="A-F5">
      <action name="Execute">
        <execute>xkill</execute>
      </action>
    </keybind>
    <keybind key="A-F10">
      <action name="Reconfigure"/>
    </keybind>
    <keybind key="A-F11">
      <action name="Restart"/>
    </keybind>
    <keybind key="A-F12">
      <action name="Exit"/>
      <prompt>no</prompt>
    </keybind>
    <keybind key="A-BackSpace">
      <action name="Exit"/>
      <prompt>yes</prompt>
    </keybind>
    <keybind key="A-Escape">
      <action name="Execute">
        <execute>xscreensaver-command --lock</execute>
      </action>
    </keybind>
    <keybind key="A-Menu">
      <action name="ShowMenu">
        <menu>client-menu</menu>
      </action>
    </keybind>
    <keybind key="XF86HomePage">
      <action name="Execute">
        <execute>firefox</execute>
      </action>
    </keybind>
    <keybind key="XF86Bluetooth">
      <action name="Execute">
        <execute>pidgin</execute>
      </action>
    </keybind>
    <keybind key="XF86Mail">
      <action name="Execute">
        <execute>thunderbird</execute>
      </action>
    </keybind>
    <keybind key="XF86Launch1">
      <action name="Execute">
        <execute>sonata</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioRaiseVolume">
      <action name="Execute">
        <execute>/home/enrico/.scripts/VolumeNotify.sh up</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioLowerVolume">
      <action name="Execute">
        <execute>/home/enrico/.scripts/VolumeNotify.sh down</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioMute">
      <action name="Execute">
        <execute>/home/enrico/.scripts/VolumeNotify.sh toggle</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioRaiseVolume">
     <action name="Execute">
       <command>amixer set Master 5%+ unmute</command>
     </action>
   </keybind>
   <keybind key="XF86AudioLowerVolume">
     <action name="Execute">
       <command>amixer set Master 5%- unmute</command>
     </action>
   </keybind>
   <keybind key="XF86AudioMute">
     <action name="Execute">
       <command>amixer set Master toggle</command>
     </action>
   </keybind>
