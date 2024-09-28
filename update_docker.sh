RESET_DB=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --reset-db) RESET_DB=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

echo "Updating the repository..."
git pull

if [ "$RESET_DB" = true ]; then
    echo "Resetting the database: dropping all tables..."
    python drop_all_tables.py --drop
else
    echo "Skipping database reset."
fi

echo "Stopping all running containers..."
docker stop $(docker ps -aq)

echo "Removing all containers..."
docker rm $(docker ps -aq)

echo "Removing all images..."
docker rmi $(docker images -q)

echo "Building and starting containers..."
docker compose up --build
