FROM confluentinc/cp-kafka-connect:5.2.2

ENV CONNECT_PLUGIN_PATH="/usr/share/java,/usr/share/confluent-hub-components"

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:latest
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.0
RUN confluent-hub install --no-prompt jcustenborder/kafka-connect-redis:0.0.2.12
RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:1.4.1
