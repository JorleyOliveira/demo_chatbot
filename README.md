## https://github.com/JorleyOliveira
## https://br.linkedin.com/in/jorleyoliveira

# train model
- cd app
- create conda env 
- install all dependecies (look: docker/bot/Dockerfile)
- activate conda env
- rasa train
- rasa test
- change name model to "result.tar.gz"

# build docker images
- execute ./build.sh

# restart docker with scale
- execute ./start.sh

# stop docker
- execute ./stop.sh

# talk with chabtot
- open http://localhost:8080

# talk 