import { useCallback } from 'react';
import { StyleSheet, Text, View, Linking, Image, Alert, Button } from 'react-native';

type SendIntentButtonProps = {
  acao: string;
  children: string;
  extras?: Array<{
    key: string;
    value: string | number | boolean;
  }>;
};

const SendIntentButton = ({
  acao,
  extras,
  children,
}: SendIntentButtonProps) => {
  const handlePress = useCallback(async () => {
    try {
      await Linking.sendIntent(acao, extras);
    } catch (e: any) {
      Alert.alert(e.message);
    }
  }, [acao, extras]);

  return <Button title={children} onPress={handlePress} />;
};
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
        <SendIntentButton acao="android.intent.action.POWER_USAGE_SUMMARY">
          Uso de bateria
        </SendIntentButton>
      </View>
      <View style={styles.section} id="sobre">
        <Text style={styles.sectionHeader}>Seção Sobre</Text>
        <Text>Conteúdo da seção Sobre.</Text>
        <SendIntentButton
          acao="android.settings.APP_NOTIFICATION_SETTINGS"
          extras={[
            {
              key: "android.provider.extra.APP_PACKAGE",
              value: "com.facebook.katana",
            },
          ]}
        >
          Configuração de notificação
        </SendIntentButton>
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
