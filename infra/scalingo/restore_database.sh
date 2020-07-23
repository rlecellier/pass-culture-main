source /config/scalingo/partial_backup/manage_tunnel.sh
ENV=$1

if [ -z "$ENV" ]
then
  echo "Please specify environment"
  exit 1
fi


kill_tunnel_if_exist $ENV
get_tunnel_database_url $ENV

echo "$(date -u +"%Y-%m-%dT%H:%M:%S") : Start partial restore DB script"
source /config/scalingo/partial_backup/partial_backup_restore.sh && echo "Partial restore completed"

kill_tunnel_if_exist $ENV