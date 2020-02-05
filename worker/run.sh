if [ "$ENV" = "development" ]; then
    worker_cmd="watchmedo auto-restart --directory=. --pattern=*.py --recursive -- $worker_cmd"
fi

bash -c "$worker_cmd"
