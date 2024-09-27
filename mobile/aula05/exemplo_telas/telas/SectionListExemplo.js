import React from 'react';
import { View, Text, SectionList, Button } from 'react-native';
import styles from '../style/estilo';
const SectionListExemplo = ({ voltaPara }) => {
    const dados = [
        { plataforma: 'Xbox', data: ['Halo', 'Forza', 'Gears of War'] },
        { plataforma: 'Playstation', data: ['God of War', 'Spiderman', 'Uncharted'] },
        { plataforma: 'Switch', data: ['Zelda', 'Metroid', 'Mario'] },
        { plataforma: 'PC', data: ['Crusaider Kings2', 'Baldur\'s gate 3', 'Mount & Blade 2'] },
        { plataforma: 'Multi', data: ['Tekken', 'Metal Gear Solid'] },
    ];
    return (
        <View style={styles.container}>
            <SectionList
                sections={dados}
                renderItem={({ item }) => <Text style={styles.item}>{item}</Text>}
                renderSectionHeader={({ section }) => (
                    <Text style={styles.sectionHeader}>{section.plataforma}</Text>
                )}
            />
            <Button title="Voltar" onPress={voltaPara} />
        </View>
    );
};
export default SectionListExemplo;
