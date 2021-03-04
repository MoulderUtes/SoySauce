#SoySauce a Arch Linux Distro
Clone git 
Install archiso package to an arch install
**Build ISO:**
	mkarchiso -v -w /(work_dir) -o /(out_dir) /(profile)
	
On line 319 there is a incorrect if statement. This line according to the comments says it should prevent path traversal outside of airootfs. This is written wrong. This line is saying if the path of airootfs_dir + passwd[5] (the home directory in the passwd file) = airootfs_dir then make the home directory and copy etc/skel. 
if [[ "$(realpath -q -- "${airootfs_dir}${passwd[5]}")" == "${airootfs_dir}"* ]]; then
If you change the code to look something like this 
if [[ "$(realpath -q -- "${airootfs_dir}${passwd[5]}")" == "${airootfs_dir}${passwd[5]}" ]]; then



Design Inspiration/Help
https://www.reddit.com/r/unixporn/comments/84wypv/lightdmwebkit2greeter_ricing_the_greeter/