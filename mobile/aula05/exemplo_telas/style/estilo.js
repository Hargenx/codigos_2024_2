import { StyleSheet } from 'react-native'; const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'lightblue',
    },
    container_sv: {
        alignItems: 'center',
        justifyContent: 'center',
    },
    item: {
        fontSize: 18,
        margin: 10,
    },
    sectionHeader: {
        fontSize: 24,
        backgroundColor: 'lightgray',
        padding: 10,
    },
    carouselContainer: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    carouselItem: {
        fontSize: 24,
    },
    page: {
        width: 400,
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    text: {
        fontSize: 24,
        fontWeight: 'bold',
        color: 'white',
    },
    pageIndicator: {
        textAlign: 'center',
        fontSize: 18,
        marginTop: 10,
    },
    buttonSpacing: {
        marginTop: 10,
    },
    button: {
        marginBottom: 10,
        width: '100%',
        height: 50,
        flexDirection: 'row',
        padding: 10,
        justifyContent: 'space-between',
    },
});
export default styles;
