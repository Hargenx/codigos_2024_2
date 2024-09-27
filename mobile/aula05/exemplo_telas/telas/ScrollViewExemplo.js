import React from 'react';
import { View, Text, ScrollView, Button } from 'react-native';
import styles from '../style/estilo';
const ScrollViewExemplo = ({ voltaPara }) => {
    const data = Array.from({ length: 20 }, (_, index) => `Contando: ${index + 1}`);
    return (
        <View>
            <ScrollView contentContainerStyle={styles.container_sv}>
                {data.map((item) => (
                    <Text style={styles.item} key={item}>
                        {item}
                    </Text>
                ))}
            </ScrollView>
            <Button title="Voltar" onPress={voltaPara} />
        </View>
    );
};
export default ScrollViewExemplo;
