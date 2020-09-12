# A shell helper function used to check and analysis our log files.
# you can just source it to use as a console command.
#
# Usage
# -----
# $ lastlog [-c|-a] [level=info] [last_n_file] [last_n_log]
#
# Flags
# -----
#     -c | --check : take a look at the last output log file.
#                  default text editor: sublime
#
#     -a | --analysis : print out filtered lines based on the log level information to console.
#                       Level assignment is needed in this situation.



function lastlog() {
    for arg in "$@"
    do
        case $arg in
            -c|--check)
            check=1
            shift
            ;;
            -a|--analysis)
            analysis=1
            shift
            ;;
            level=*)
            LEVEL=$(echo "${arg#*=}" | tr '[:lower:]' '[:upper:]')
            shift
            ;;
        esac
    done

    log_root="./log"
    last_n_file=$(command ls -t $log_root | head -n ${1:-1} | tail -n 1)
    last_n_log=$(command ls -t $log_root/$last_n_file | head -n ${2:-1} | tail -n 1)

    if [[ check -eq 1 ]]; then
        subl "${log_root}/${last_n_file}/${last_n_log}"
    fi

    if [[ analysis -eq 1 ]]; then
        if [ LEVEL ]; then
            grep -w $LEVEL "${log_root}/${last_n_file}/${last_n_log}"
        else
            echo "level flag assignment expected"; exit 1
        fi
    fi
}
