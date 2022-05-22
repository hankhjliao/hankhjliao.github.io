---
Title: Template
Date: 2022-06-01 11:20
Category: Template
Tags: Template
Slug: template
Summary: Summary of template
Lang: en
Status: draft
Password: mydraft
---

[TOC]

## Normal

==Highlight==

> ==highlight==
> **bold**
> *italic*
>
> Test

ThisLineIsVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongEND[^1]


[^1]: ThisLineIsVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongVeryLongEND

https://www.example.com/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/very/long/END/


中文夾雜English測試

## Image

![The transliteration option in goldendict with opencc support.]({attach}/images/add-opencc-support-for-goldendict-in-archlinux-option.png "image title")

## Math

$E = mc^2$

$$
\lim_{x\rightarrow0} \frac{\sin(x)}{x} = 1 \newline
\int\limits_a^b {\frac{d}{{dx}}F\left( x \right)dx} = F\left( b \right) - F\left( a \right) \newline
s_N = \sqrt {\frac{1}{N}\sum\limits_{i = 1}^N {\left( {x_i - \bar x} \right)^2 } } \newline
\left\{
\begin{align}
    \nabla \cdot \mathbf{E} &= \cfrac{\rho}{\varepsilon_0} \\
    \nabla \cdot \mathbf{B} &= 0 \\
    \nabla \times \mathbf{E} &= -\cfrac{\partial \mathbf{B}}{\partial t} \\
    \nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\varepsilon_0 \cfrac{\partial \mathbf{E}}{\partial t}
\end{align}
\right.
$$


## Code

++Ctrl+B++

`inline code`

``` diff
...
- depends=('hunspell' 'libxtst' 'libzip' 'libao' 'qt5-webkit' 'qt5-svg' 'qt5-x11extras' 'qt5-tools' 'phonon-qt5' 'ffmpeg')
+ depends=('hunspell' 'libxtst' 'libzip' 'libao' 'qt5-webkit' 'qt5-svg' 'qt5-x11extras' 'qt5-tools' 'phonon-qt5' 'ffmpeg' 'opencc')
...
build(){
    cd "${srcdir}"/$pkgname-1.5.0-RC2
-   qmake-qt5 "CONFIG+=no_epwing_support" PREFIX="/usr"
+   qmake-qt5 "CONFIG+=no_epwing_support chinese_conversion_support" PREFIX="/usr"

    make
}
...
```

```console
root@ubuntu:~# id
uid=0(root) gid=0(root) groups=0(root)
root@ubuntu:~#
```

```python
print("Hello world")
```

```cpp hl_lines="1 3"
#include <iostream>
using namespace std;
int main(void) {
    cout << "Hello world" << endl;
    return 0;
}
```

```hexdump
00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  02 00 3e 00 01 00 00 00  c5 48 40 00 00 00 00 00  |..>......H@.....|
```


## Admonition

!!! type "optional explicit title within double quotes"
    Any number of other indented markdown elements.

    This is the second paragraph.


<!-- danger, error -->
!!! danger "Don't try this at home"
    ...

<!-- warning, caution, attention -->
!!! warning
    ...

<!-- note, important -->
!!! note
    ...

<!-- hint, tip -->
!!! tip
    ...

<!-- nested -->
!!! note
    !!! tip
        ...
    ...



## More Information

- https://python-markdown.github.io/extensions/