import React from 'react';
import { View, Text, FlatList, Button } from 'react-native';
import styles from '../style/estilo';
const FlatListExemplo = ({ voltaPara }) => {
    const dado = Array.from({ length: 100 }, (_, index) => ({ key: index.toString(), value: index + 1 })
    ); return (
        <View style={styles.container}>
            <FlatList
                data={dado}
                renderItem={({ item }) => <Text style={styles.item}>Item {item.value}</Text>}
            />
            <Button title="Voltar" onPress={voltaPara} />
        </View>
    );
};
export default FlatListExemplo;
