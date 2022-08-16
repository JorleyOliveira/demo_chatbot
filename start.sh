#bin/sh

docker-compose -f docker-compose.yml -p serasa up -d --scale rasa=3 