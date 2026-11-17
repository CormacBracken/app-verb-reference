import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { Button, StyleSheet, Text, TextInput, View } from 'react-native';

export default function App() {
  const [verb, setVerb] = useState('');
  const [result, setResult] = useState('Enter a verb to test bundled lookup.');
  return (
    <View style={styles.container}>
      <Text accessibilityRole="header">Toolchain smoke</Text>
      <TextInput
        accessibilityLabel="Verb"
        testID="verb-input"
        placeholder="Verb"
        value={verb}
        onChangeText={setVerb}
        autoCapitalize="none"
        style={styles.input}
      />
      <Button title="Look up" onPress={() => setResult(
        verb.trim().toLowerCase() === 'hablar' ? 'hablo — I speak' : 'No fixture found'
      )} />
      <Text testID="lookup-result" accessibilityLiveRegion="polite">{result}</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    gap: 24,
  },
  input: { borderWidth: 1, borderColor: '#555', width: '100%', padding: 12, fontSize: 20 },
});
