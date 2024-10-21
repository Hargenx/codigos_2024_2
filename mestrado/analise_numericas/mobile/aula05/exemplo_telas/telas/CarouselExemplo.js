import React, { useState } from 'react';
import { View, Text, Button, ScrollView } from 'react-native';
import styles from '../style/estilo';

const CarouselExemplo = ({ voltaPara }) => {
    const [currentPage, setCurrentPage] = useState(0);
    const paginas = [
        { backgroundColor: 'skyblue', text: 'Página 1' },
        { backgroundColor: 'lightgreen', text: 'Página 2' },
        { backgroundColor: 'lightcoral', text: 'Página 3' },
    ];
    const handlePageChange = (event) => {
        const offset = event.nativeEvent.contentOffset.x;
        const currentIndex = Math.round(offset / 400);
        setCurrentPage(currentIndex);
    };
    return (
        <View style={styles.container}>
            <ScrollView
                horizontal
                pagingEnabled
                showsHorizontalScrollIndicator={false}
                onMomentumScrollEnd={handlePageChange}
                style={styles.scrollView}
            >
                {paginas.map((page, index) => (
                    <View
                        key={index}
                        style={[styles.page, { backgroundColor: page.backgroundColor }]}
                    >
                        <Text style={styles.text}>{page.text}</Text>
                    </View>
                ))}
            </ScrollView>
            <Text style={styles.pageIndicator}>
                Página {currentPage + 1} de {paginas.length}
            </Text>
            <Button title="Voltar" onPress={voltaPara} />
        </View>
    );
};
export default CarouselExemplo;