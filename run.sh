if [ ! -f .env ]
then
  export $(cat .env.dev | xargs)
fi

echo "" > run.log

function kill() {
  echo "killing running instances"
  pkill python
}
trap "kill" 2

echo "running consumer ..."
pushd consumer
nohup python run.py >> ../run.log 2>&1 &
popd

echo "running producer ..."
pushd producer
nohup python run.py >> ../run.log 2>&1 &
popd

tail -fn100 run.log