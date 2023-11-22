export i=0; while true; do echo "{\"level\":\"info\",\"time\":$(date +%s),\"msg\":\"I like rapadura ${i}\"}" >> ./shared/generated-log.log; i=$((i+1));sleep 5;done
