
source /config/scalingo/partial_backup/manage_tunnel.sh
ENV=$1

if [ -z "$ENV" ]
then
  echo "Please specify environment"
  exit 1
fi

kill_tunnel_if_exist $ENV
get_tunnel_database_url $ENV

echo "$(date -u +"%Y-%m-%dT%H:%M:%S") : Start database drop"

# Check if the tunnel has been created
if [ -z "$tunnel_database_url" ]
then
  echo "Can not create tunnel ssh from environment"
  exit 1
fi

time psql $tunnel_database_url -a -f /config/scalingo/clean_database.sql \
&& echo "Database dropped" || failure_alert "Database drop"
echo "$(date -u +"%Y-%m-%dT%H:%M:%S") : End of database drop"

kill_tunnel_if_exist $ENV