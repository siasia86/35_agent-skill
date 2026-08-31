#!/usr/bin/env bash
WHO01="$(pwd | awk -F'/' '{print $3}')"

echo "rsync -av /home/sjyun/.kiro/ /root/sj_del/00_default/.kiro/ --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n"
echo "rsync -av /home/yunli/.kiro/ /root/sj_del/00_default/.kiro/ --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n"

echo "============================================="
echo "# rsync --dry-run mode #"
#echo "rsync -av /home/${WHO01}/.kiro/ /root/sj_del/00_default/.kiro/          --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n"
echo  "rsync -av /home/${WHO01}/.kiro/ /root/sj_del/00_default/.kiro/${WHO01}/ --exclude .cli_bash_history --exclude sessions --exclude *.swp -n"
echo "============================================="

rsync -av /home/${WHO01}/.kiro/ /root/sj_del/00_default/.kiro/${WHO01}/ --exclude .cli_bash_history --exclude sessions --exclude settings --exclude *.swp  -n
for ((i=1;i<=10;i++)) ; do echo "#####  ${i}  #####" ; sleep 1 ; done
rsync -av /home/${WHO01}/.kiro/ /root/sj_del/00_default/.kiro/${WHO01}/ --exclude .cli_bash_history --exclude sessions --exclude settings --exclude *.swp

echo "rsync --dry-run"
rsync -av /home/${WHO01}/.kiro/ /root/35_agent-skill/kiro/  --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp --exclude 01_home-sjyun-kiro.sh --exclude settings -n
for ((i=1;i<=5;i++)) ; do echo "#####  ${i}  #####" ; sleep 1 ; done
rsync -av /home/${WHO01}/.kiro/ /root/35_agent-skill/kiro/  --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp --exclude 01_home-sjyun-kiro.sh --exclude settings


##################################################

#rsync -av  /root/sj_del/00_default/.kiro/siasia/ /home/sjyun/.kiro/ --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n && chown -R sjyun:sjyun /home/sjyun/.kiro

#rsync -av  /root/sj_del/00_default/.kiro/siasia/ /home/yunli/.kiro/ --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n && chown -R yunli:yunli /home/yunli/.kiro

#rsync -av  /root/sj_del/00_default/.kiro/siasia/ /home/siasia/.kiro/ --exclude .cli_bash_history --exclude sessions --exclude .local --exclude *.swp  -n && chown -R siasia:siasia /home/siasia/.kiro

## diff -r /home/sjyun/.kiro/ /home/yunli/.kiro/  --exclude='.cli_bash_history' --exclude='sessions'

