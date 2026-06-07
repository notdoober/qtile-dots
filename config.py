from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

C_BG = "#1a1b26"
C_INACTIVE = "#414868"
C_OCCUPIED = "#9aa5ce"
C_ACTIVE = "#c0caf5"

keys = [
    Key([mod], "q", lazy.spawn(terminal)),
    Key([mod], "d", lazy.spawn(
        "dmenu_run "
        "-fn 'Iosevka Nerd Font-14:bold' "
        "-nb '#1a1b26' "
        "-nf '#a9b1d6' "
        "-sb '#7aa2f7' "
        "-sf '#1a1b26'"
    )),
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "Print", lazy.spawn("scrot '%Y-%m-%d-%H%M%S_screenshot.png' -e 'mv $f ~/Pictures/Screenshots/'")),
    Key([mod], "r", lazy.spawn("alacritty -e ranger")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_on_single": True,
    "border_focus": C_ACTIVE,
    "border_normal": C_BG,
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
]

widget_defaults = {
    "font": "Iosevka Nerd Font Bold",
    "fontsize": 13,
    "padding": 10,
    "background": C_BG,
    "foreground": C_ACTIVE,
}
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="[N]",
                    foreground=C_ACTIVE,
                    padding=14,
                ),
                widget.GroupBox(
                    active=C_OCCUPIED,
                    inactive=C_INACTIVE,
                    highlight_method="text",
                    this_current_screen_border=C_ACTIVE,
                    disable_drag=True,
                    padding=8,
                    borderwidth=0,
                ),
                widget.Spacer(),
                widget.Clock(
                    format="%a %b %d  %H:%M",
                    foreground=C_OCCUPIED,
                    padding=14,
                    update_interval=1,
                ),
            ],
            32,
        ),
        left=bar.Gap(2),
        right=bar.Gap(2),
        bottom=bar.Gap(2),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=C_ACTIVE,
    border_normal=C_BG,
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

