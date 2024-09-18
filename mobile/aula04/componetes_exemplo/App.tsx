import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={require("./assets/img/image.png")} style={styles.logo} />
      <Text style={styles.header}>Meu APP! 💓 </Text>
      <View style={styles.nav}>
        <Text
          style={styles.navLink}
          onPress={() => console.log("Clique Inicio")}
        >
          INICIO
        </Text>
        <Text
          style={styles.navLink}
          onPress={() => console.log("Clique Momento")}
        >
          MOMENTO
        </Text>
        <Text
          style={styles.navLink}
          onPress={() => console.log("Clique Sobre")}
        >
          SOBRE
        </Text>
        <Text
          style={styles.navLink}
          onPress={() => console.log("Clique Contato")}
        >
          CONTATO
        </Text>
      </View>
      <View style={styles.section} id="inicio">
        <Text style={styles.sectionHeader}>Seção de Início</Text>
        <Text>Conteúdo da seção de Início.</Text>
        <Text>... </Text>
      </View>
      <View style={styles.section} id="sobre">
        <Text style={styles.sectionHeader}>Seção Sobre</Text>
        <Text>Conteúdo da seção Sobre.</Text>
        <Text>...</Text>
      </View>
      <View style={styles.section} id="contato">
        <Text style={styles.sectionHeader}>Seção de Contato</Text>
        <Text>Conteúdo da seção de Contato.</Text>
        <Text>...</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  logo: {
    width: 40,
    height: 40,
    marginRight: 10,
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 20,
  },
  nav: {
    flexDirection: "row",
    justifyContent: "center",
    marginBottom: 20,
  },
  navLink: {
    marginHorizontal: 10,
    color: "blue",
  },
  section: {
    marginBottom: 30,
  },
  sectionHeader: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 10,
  },
});
