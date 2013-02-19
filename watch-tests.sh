#!/bin/bash
clear
cmd="nosetests --with-alert"
$cmd
watchmedo shell-command -R -p "*.py" -c "clear && $cmd" .

