---
Title: Enlarge the EFI System Partition on a Dual Boot System (Arch Linux + Windows)
Date: 2024-03-07T23:00:00
Tags: [tutorial]
---

{{<notice warning>}}
After modifying the EFI System Partition (ESP), you might need to rebuild Windows boot configuration data (BCD).
{{</notice>}}

## Prerequisite

- Bootable USB with Arch Linux live environment
- Bootable USB with Windows installation ISO

If your computer uses the new Intel Volume Management Device (VMD) technology:
- USB with the Intel Rapid Storage Technology (IRST) driver package inside
- Or, Bootable USB with Windows installation ISO provided by the computer manufacturer instead

## Enlarge the EFI System Partition (ESP) in the Arch Linux Live Environment

1. Boot the computer with Arch Linux live environment
2. Use a partitioning tool like `parted` to make room for the ESP
3. Mount the ESP:

    `# mount /dev/sdx1 /mnt` # replace sdx1 with ESP

4. Backup the contents of the ESP:

    `# mkdir ~/esp`

    `# rsync -av /mnt/ ~/esp/`

5. Unmount the ESP:

    `# umount /mnt`

6. Delete and recreate the ESP:

    ```bash
    gdisk /dev/sdx # replace sdx with disk containing ESP
    p (list partitions)
    (ensure the ESP is the first partition)
    d (delete partition)
    1 (select first partition)
    n (create partition)
    Enter (use default partition number, should be 1)
    Enter (use default first sector, should be 2048)
    Enter (use default last sector, should be all available space)
    EF00 (hex code for EFI system partition)
    w (write changes to disk and exit)
    ```

7. Format the ESP:

    `# mkfs.fat -F32 /dev/sdx1`

8. Restore the contents of the ESP:

    `# mount /dev/sdx1 /mnt`

    `# rsync -av ~/esp/ /mnt`

9. Unmount the ESP:

    `# umount /mnt`

10. Mount the root volume of the installed Arch Linux

    `# mount /dev/sdx2 /mnt` # replace sdx2 with root volume

11. Change root into the Arch Linux

    `# arch-chroot /mnt`

12. Get the new UUID of the ESP

    `# blkid | grep EFI`

13. Update EFI entry in `/etc/fstab` of Arch Linux

    ```bash
    UUID=XXXX-XXXX /boot vfat umask=0077 0 2 # Replace with UUID from blkid
    ```

14. Update GRUB

    `# grub-mkconfig -o /boot/grub/grub.cfg`

## Rebuild Windows boot configuration data (BCD) in Windows Installation Environment

{{<notice note>}}
If your computer uses the new Intel Volume Management Device (VMD) technology:

a. You may need to prepare another USB with the Intel Rapid Storage Technology (IRST) driver package inside.

b. Or, use the Windows installation ISO provided by the computer manufacturer, e.g., Dell provides the Windows installation ISO with basic drivers.
> [Dell media](https://www.dell.com/support/kbdoc/en-us/000123667/how-to-download-and-use-the-dell-os-recovery-image-in-microsoft-windows) does include basic drivers for RAID controllers, so if a RAID is deleted and partitions are cleared, the installation media will recreate partitions and install Windows 10 without the need for additional driver installations.
> 
> --- [link](https://www.dell.com/support/kbdoc/en-us/000146119/windows-10-command-line-driver-install-for-dell-media-missing-nvme-driver)
{{</notice>}}

1. Boot the computer with the Windows installation environment
2. Open the command prompt
3. Use `diskpart` to check whether the Windows installed volume is visible

    ```cmd
    > diskpart
    diskpart> list disk
    diskpart> select disk disk_num # disk_num is the disk where you installed windows
    diskpart> list volume
    diskpart> exit
    ```

4. Backup the BCD of the Windows Installation Environment

    `> ren BCD BCD.bak`

5. Rebuild BCD

    `> bootrec /rebuildbcd`

6. Boot the computer with installed Arch Linux

7. Update GRUB for the new Windows BCD

    `$ sudo grub-mkconfig -o /boot/grub/grub.cfg`

## Reference & More Information

- https://superuser.com/questions/1230741/how-to-resize-the-efi-system-partition
- https://www.lifewire.com/how-to-rebuild-the-bcd-in-windows-2624508
- https://www.dell.com/support/kbdoc/en-us/000123667/how-to-download-and-use-the-dell-os-recovery-image-in-microsoft-windows
- https://www.dell.com/support/kbdoc/en-us/000146119/windows-10-command-line-driver-install-for-dell-media-missing-nvme-driver
- https://www.dell.com/support/kbdoc/en-us/000188116/intel-11th-generation-processors-no-drives-can-be-found-during-windows-10-installation