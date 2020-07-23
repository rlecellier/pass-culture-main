
source /config/scalingo/partial_backup/manage_tunnel.sh
ENV=$1

if [ -z "$ENV" ]
then
  echo "Please specify environment"
  exit 1
fi

kill_tunnel_if_exist $ENV
get_tunnel_database_url $ENV

echo "$(date -u +"%Y-%m-%dT%H:%M:%S") : Start anonymization"
TUNNEL_PORT=$TUNNEL_PORT TARGET_USER=$PG_USER TARGET_PASSWORD=$PG_PASSWORD bash /config/scalingo/anonymize_database.sh -a "$app_name" \
&& echo "Anonymized" || failure_alert "Anonymization"

kill_tunnel_if_exist $ENV