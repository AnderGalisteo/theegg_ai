#!/bin/bash
# dontforget
#
# A stupid script for short term reminders in bash
#
# Arguments just need to contain a number and a bunch of words.
#
# The number can be anywhere in the arguments, but there shouldn't
# be any other numeric digits.
#
# If the number has h, m, or s immediately after it (no space), it will
# be interpreted as hours, minutes, or seconds. The default assumption
# is minutes.
#
# Save the script as `dontforget` in your path and make it executable
#
# Usage
# 	$ dontforget let the dog back inside 10
# 	=> I'll remind you: "let the dog back inside" in 10 minutes
#
# It can parse a little extra verbosity around the text, too
# 	$ dontforget to let my dog back inside in 10m
# 	=> I'll remind you: "let your dog back inside" in 10 minutes
#
# 	$ dontforget I really need to take a break in 1h
# 	I'll remind you: "you really need to take a break" in 60 minutes
#
# Running dontforget with no arguments will list upcoming reminders
#
# Use `dontforget cancel` or `dontforget nevermind` to cancel the last
# reminder that was created
#
# $ dontforget cancel
# Canceled "you really need to take a break"
#
# To turn on LaunchBar "large text" display
# export DF_LAUNCHBAR=true
#
# To make dontforget remain in the foreground and cancelable with ^c
# export DF_NO_BACKGROUND=true
#
# Tip:
# alias forget="dontforget cancel"

[[ -z $DF_LAUNCHBAR ]] && DF_LAUNCHBAR=false || $DF_LAUNCHBAR
[[ -z $DF_NO_BACKGROUND ]] && DF_NO_BACKGROUND=false || $DF_NO_BACKGROUND

__df() {
	if [[ $# == 0 ]]; then
		__df_list_reminders
		return
	fi

	if [[ $# == 1 && $1 =~ (cancel|nevermind) ]]; then
		__df_cancel
		return $?
	fi

	local timespan reminder
	for arg in $@; do
		# e.g. 3:30pm, 10am -- parse as date
		if [[ $arg =~ ^[0-9][0-9]?(:[0-9][0-9])?(a|p)m?$ && -z $timespan ]]; then
			# ensure meridian (2a = 2am)
			arg=$(echo "$arg"|sed -E 's/m?$/m/')
			timespan=$(__df_parse_date $arg)
		# e.g. 1h or 30m -- parse as interval
		elif [[ $arg =~ ^[0-9]+[hms]?$ && -z $timespan ]]; then
			timespan=$(echo "$arg"|sed -E 's/^([0-9]+)([HhSsMm])?$/\1 \2/')
		# Assume part of reminder string
		else
			reminder+=" $arg"
		fi
	done

	length=${timespan%% *}
	unit=${timespan#* }

	if [[ $unit == "h" ]]; then
		length=$(($length*60*60))
	elif [[ $unit != "s" ]]; then
		length=$(($length*60))
	fi
	reminder=$(__df_clean_reminder "$reminder")

	# echo "I'll remind you: \"$reminder\" in $(($length/60)) minutes"
	echo "I'll remind you: \"$reminder\" in $(__df_show_time $length)"
	if [[ $DF_NO_BACKGROUND == true ]]; then
		sleep $length && __df_remind "$reminder"
	else
		sleep $length && __df_remind "$reminder" &
	fi
}

__df_parse_date() {
	TIMESTAMP=$(ruby -rtime -e "puts Time.parse('$1').strftime('%s')")
	NOW=$(date '+%s')
	echo "$(($TIMESTAMP-$NOW)) s"
}

__df_list_reminders() {
	IFS=$'\n'; for line in $(ps ax | grep -E "bash .*?dontforget \w+" | grep -v grep); do echo $(__df_clean_reminder $(echo "$line" | sed -E 's/.*dontforget //')); done
}

__df_remind() {
	local reminder="$*"
	if [[ -n $(ps ax | grep LaunchBar.app) && $DF_LAUNCHBAR == true ]]; then
		osascript -e "tell application \"LaunchBar\" to display in large type \"Time to $reminder\" with sound \"Glass\""
	else
		osascript -e "display dialog \"Time to $reminder\""
	fi
	/usr/bin/afplay /System/Library/Sounds/Glass.aiff
	say "$reminder"
}

__df_clean_reminder() {
	local input="$*"
	# trim whitespace
	input=$(echo -e "$input" | sed -E 's/(^ *| *$)//g') | tr -s ' '
	# change " I " to " you "
	input=$(echo -e "$input" | sed -E 's/(^| +)[Ii]( +|$)/\1you\2/g')
	# change " my " to " your "
	input=$(echo -e "$input" | sed -E 's/(^| +)[Mm]y( +|$)/\1your\2/g')
	# strip leading "forget" in case you alias to dont, i.e. "dont forget to..."
	input=$(echo -e "$input" | sed -E 's/^ *forget//')
	# strip extra words from natural language
	local output=$(__df_strip_naturals "$input")

	# final whitespace trim
	echo -e "$output" | sed -E 's/(^ *| *$)//g' | tr -s ' '
}

__df_strip_naturals() {
	local original=$(echo "$*"|sed -E 's/^( *remind me *)//')
	while [[ "$original" =~ ^[[:space:]]*(to|in|about|at) ]]; do
		original=$(echo "$original"| sed -E 's/^ *(to|in|about|at) *//g')
	done

	[[ "$original" =~ in[[:space:]]*$ ]] && original=$(echo "$original"| sed -E 's/ *in *$//')
	# [[ "$original" =~ at[[:space:]]*$ ]] && original=$(echo "$original"| sed -E 's/ *at *$//')

	echo $original  | sed -E 's/(^ *| *$)//g'
}

__df_show_time () {
	local num=$1
	local sec=0
	local min=0
	local hour=0
	local day=0
	local output=""
	if ((num>59)); then
		((sec=num%60))
		if ((sec>0)); then
			output="${sec} $(__df_pluralize $sec second) $output"
		fi
		((num=num/60))

		if((num>59)); then
			((min=num%60))
			if ((min>0)); then
				output="${min} $(__df_pluralize $min minute) $output"
			fi
			((num=num/60))
			if((num>23)); then
				((hour=num%24))
				if ((hour>0)); then
					output="${hour} $(__df_pluralize $hour hour) $output"
				fi

				((day=num/24))
				if ((day>0)); then
					output="${day} $(__df_pluralize $day day) $output"
				fi
			else
				((hour=num))
				output="${hour} $(__df_pluralize $hour hour) $output"
			fi
		else
			((min=num))
			output="${min} $(__df_pluralize $min minute) $output"
		fi
	else
		((sec=num))
		output="${sec} $(__df_pluralize $sec sec) $output"
	fi
	echo $output
}

__df_pluralize() {
	if (($1>1)); then
		echo "${2}s"
	else
		echo $2
	fi
}

__df_cancel() {
	local df_job=$(ps ax | grep dontforget | grep -v grep | grep -v cancel | grep -v nevermind | tail -n 1)

	if [[ -z $df_job || $df_job == "" ]]; then
		echo "No timer found"
		return 1
	else
		local pid=$(echo "$df_job" | awk '{print $1}')
		kill $pid
		local title=$(echo "$df_job" | sed -E 's/.*dontforget (.*)$/\1/')
		echo "Canceled \"$(__df_clean_reminder "$title")\""
	fi
}

__df $@