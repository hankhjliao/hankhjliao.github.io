Fix Dark Text on Dark Background of QT Apps in Gnome with Dark Theme
####################################################################
:date: 2021-07-14 20:00
:category: Tutorial
:tags: tutorial
:slug: 2021-07-14-fix-dark-text-on-dark-background-of-qt-apps-in-gnome-with-dark-theme
:summary: When we change the theme of the QT apps to the dark varient, the text of the interference might be difficult to see on the dark background.

Problem
=======

When we change the theme of the QT apps to the dark varient, the text of the interference might be difficult to see on the dark background.

.. raw:: html

   <div class="text-center">
   <figure class="figure">
   <img src="{attach}/images/fix-dark-text-in-dark-theme-using-qt-in-gnome-1.png" class="figure-img img-fluid rounded" alt="Dark text on dark background (Goldendict)">
   <figcaption class="figure-caption text-center">Dark text on dark background (Goldendict)</figcaption>
   </figure>
   </div>

Solution
========

#. Install Tools: :code:`$ yay -S kvantum-qt5 qt5ct qt5-styleplugins`

#. Add the content below in ``~/.profile``:

   .. code-block:: sh

      export QT_QPA_PLATFORMTHEME=gtk2
      export QT_STYLE_OVERRIDE=kvantum

#. Select preferred dark theme in kvantum.

   .. raw:: html

      <div class="text-center">
      <figure class="figure">
      <img src="{attach}/images/fix-dark-text-in-dark-theme-using-qt-in-gnome-4.png" class="figure-img img-fluid rounded" alt="Select preferred dark theme">
      <figcaption class="figure-caption text-center">Select preferred dark theme</figcaption>
      </figure>
      </div>

#. Change ``kvantum`` to ``kvantum-dark`` in the QT5 Setting as below:

   .. raw:: html

      <div class="text-center">
      <figure class="figure">
      <img src="{attach}/images/fix-dark-text-in-dark-theme-using-qt-in-gnome-3.png" class="figure-img img-fluid rounded" alt="Change kvantum to kvantum-dark">
      <figcaption class="figure-caption text-center">Change kvantum to kvantum-dark</figcaption>
      </figure>
      </div>

.. note::
  Sometimes you will need to logout and login again to apply the new settings.

Result
======

.. raw:: html

   <div class="text-center">
   <figure class="figure">
   <img src="{attach}/images/fix-dark-text-in-dark-theme-using-qt-in-gnome-2.png" class="figure-img img-fluid rounded" alt="Interface after fix (Goldendict)">
   <figcaption class="figure-caption text-center">Interface after fix (Goldendict)</figcaption>
   </figure>
   </div>
