// mikie Reed 8.3.2020
// take a string like ab and return aab
// ex: input "Code" return "CCoCodCode"

public String stringSplosion(String str) {
  String splosion = "";
  for (int i = 0; i <= str.length(); ++i) {
    splosion += str.substring(0, i);
  }
  return splosion;
}