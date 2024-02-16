---
Title: Fix Dark Text on Dark Background of QT Apps in Gnome with Dark Theme
Date: 2021-07-14T20:00:00
Categories: Tutorial
Tags: tutorial
Slug: 2021-07-14-fix-dark-text-on-dark-background-of-qt-apps-in-gnome-with-dark-theme
Summary: When we change the theme of the QT apps to the dark varient, the text of the interference might be difficult to see on the dark background.
---

## Problem

When we change the theme of the QT apps to the dark varient, the text of the interference might be difficult to see on the dark background.

{{< figure src="fix-dark-text-in-dark-theme-using-qt-in-gnome-1.png" caption="Dark text on dark background (Goldendict)" >}}

## Solution

1. Install Tools: `$ yay -S kvantum-qt5 qt5ct qt5-styleplugins`

2. Add the content below in ``~/.profile``:

   ```sh
   export QT_QPA_PLATFORMTHEME=gtk2
   export QT_STYLE_OVERRIDE=kvantum
   ```

3. Select preferred dark theme in kvantum.

   {{< figure src="fix-dark-text-in-dark-theme-using-qt-in-gnome-4.png" caption="Select preferred dark theme" >}}

4. Change ``kvantum`` to ``kvantum-dark`` in the QT5 Setting as below:

   {{< figure src="fix-dark-text-in-dark-theme-using-qt-in-gnome-3.png" caption="Change kvantum to kvantum-dark" >}}

.. note::
  Sometimes you will need to logout and login again to apply the new settings.

## Result

{{< figure src="fix-dark-text-in-dark-theme-using-qt-in-gnome-2.png" caption="Interface after fix (Goldendict)" >}}
