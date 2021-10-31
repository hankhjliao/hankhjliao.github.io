---
Title: [Fontconfig] Fix TW-Kai Pollution
Date: 2021-10-31 19:20
Category: Tutorial
Tags: Tutorial
Slug: fontconfig-fix-tw-kai-pollution
Summary: Fontconf: Fix TW-Kai Pollution
---

## Problem

<div class="text-center">
  <figure class="figure">
    <img src="{attach}/images/fontconfig-fix-tw-kai-pollution-1.png" class="figure-img img-fluid rounded" alt="TW-Kai pollutes the monospace font in the gnome terminal.">
    <figcaption class="figure-caption text-center">TW-Kai pollutes the monospace font in the gnome terminal.</figcaption>
  </figure>
</div>

For the sake of displaying most of the CJK characters in Linux, you might get the solution of installing `TW-Kai` and `TW-Sung` fonts after googling.
However, some applications may look strange after installing them.

## Solution

If the font cannot display the character, it will ask other fonts for help. And there is an order to ask for help.
Unfortunately, the priority of `TW-Kai` and `TW-Sung` is higher than the other CJK fonts in some Linux distributions.
Therefore, we can fix the problem by setting the default fonts and adjusting the fallback order.

Edit `~/.config/fontconfig/fonts.conf` like below:

<details>

<summary>Click to show the fonts.conf</summary>

<br>

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

<fontconfig>

    <!-- Default serif fonts -->
    <match>
        <test name="family">
            <string>serif</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>Noto Serif</string>
            <string>Noto Serif CJK TC</string>
            <string>Noto Serif CJK SC</string>
            <string>Noto Serif CJK JP</string>
            <string>Noto Serif CJK KR</string>
        </edit>
    </match>

    <!-- Default sans-serif font -->
    <match>
        <test name="family">
            <string>sans-serif</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>Noto Sans</string>
            <string>Noto Sans CJK TC</string>
            <string>Noto Sans CJK SC</string>
            <string>Noto Sans CJK JP</string>
            <string>Noto Sans CJK KR</string>
        </edit>
    </match>

    <!-- Default monospace fonts -->
    <match>
        <test name="family">
            <string>monospace</string>
        </test>
        <edit name="family" mode="prepend" binding="strong">
            <string>Inconsolata</string>
            <string>Noto Sans Mono CJK TC</string>
            <string>Noto Sans Mono CJK SC</string>
            <string>Noto Sans Mono CJK JP</string>
            <string>Noto Sans Mono CJK KR</string>
        </edit>
    </match>

    <!-- Fallback fonts preference order -->
    <alias>
        <family>serif</family>
        <prefer>
            <family>Noto Serif</family>
            <family>Noto Serif CJK TC</family>
            <family>Noto Serif CJK SC</family>
            <family>Noto Serif CJK JP</family>
            <family>Noto Serif CJK KR</family>
            <family>Noto Color Emoji</family>
            <family>Noto Emoji</family>
        </prefer>
        <default>
            <family>TW-Sung</family>
            <family>TW-Sung-Plus</family>
            <family>TW-Sung-Ext-B</family>
            <family>TW-Kai</family>
            <family>TW-Kai-Plus</family>
            <family>TW-Kai-Ext-B</family>
        </default>
    </alias>
    <alias>
        <family>sans-serif</family>
        <prefer>
            <family>Noto Sans</family>
            <family>Noto Sans CJK TC</family>
            <family>Noto Sans CJK SC</family>
            <family>Noto Sans CJK JP</family>
            <family>Noto Sans CJK KR</family>
            <family>Noto Color Emoji</family>
            <family>Noto Emoji</family>
        </prefer>
        <default>
            <family>TW-Sung</family>
            <family>TW-Sung-Plus</family>
            <family>TW-Sung-Ext-B</family>
            <family>TW-Kai</family>
            <family>TW-Kai-Plus</family>
            <family>TW-Kai-Ext-B</family>
        </default>
    </alias>
    <alias>
        <family>monospace</family>
        <prefer>
            <family>Inconsolata</family>
            <family>Noto Sans Mono</family>
            <family>Noto Sans Mono CJK TC</family>
            <family>Noto Sans Mono CJK SC</family>
            <family>Noto Sans Mono CJK JP</family>
            <family>Noto Sans Mono CJK KR</family>
            <family>Noto Color Emoji</family>
            <family>Noto Emoji</family>
        </prefer>
        <default>
            <family>TW-Sung</family>
            <family>TW-Sung-Plus</family>
            <family>TW-Sung-Ext-B</family>
            <family>TW-Kai</family>
            <family>TW-Kai-Plus</family>
            <family>TW-Kai-Ext-B</family>
        </default>
    </alias>

</fontconfig>
```

</details>

<br>

After editing the fonts.conf, you need to run `$ fc-cache -f` to rebuild the font cache.

You can check the order by `$ fc-match -s serif`, `$ fc-match -s sans-serif`, and `$ fc-match -s monospace`.

!!! note
    `<alias>` is the shortcut to adjust the priority of the fallback fonts.
    
    In the end, the order will be like this: `<prefer> -> original -> <accept> -> <default>`

## More Information

- `TW-Kai` and `TW-Sung`: https://data.gov.tw/dataset/5961
- https://www.freedesktop.org/software/fontconfig/fontconfig-user.html
- https://wiki.archlinux.org/title/Font_configuration