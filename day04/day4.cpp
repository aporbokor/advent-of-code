#include <iostream>
#include <fstream>  
using namespace std;

string fileName = "day4.in2";

int main() {
  ifstream file(fileName);
  string line;
  int sum = 0;
  while (getline(file, line)) {
    
    int yourNumbersLength = -1;
    int winningNumbersLength = 0;
    bool halfPoint = false;
    for (int i = 0; i < line.length(); i++) {
      if (line[i] == '|') {
        halfPoint = true;
      } else if (isdigit(line[i]) && !isdigit(line[i-1])) {
        if (halfPoint) {
          winningNumbersLength++;
        } else {
          yourNumbersLength++;
        }
      }
    }
    
    int yourNumbers[yourNumbersLength];
    int winningNumbers[winningNumbersLength];
    string currentNumber;
    int counter = -1;
    for (int i = 0; i < line.length(); i++) {
      if (isdigit(line[i])) {
        currentNumber += line[i];
      } 
      if ((line[i] == ' ' && isdigit(line[i-1])) || i == line.length() - 1) {
        counter++;
        if (counter < yourNumbersLength) {
          yourNumbers[counter] = stoi(currentNumber);
        } else {
          winningNumbers[counter - yourNumbersLength] = stoi(currentNumber);
        }
        currentNumber = "";
      } else if (line[i] == ':') {
        currentNumber = "";
      }
    }

    //for (auto x : yourNumbers) cout << x << " ";
    //cout << " printing winningnumbers" << endl;
    //for (auto x : winningNumbers) cout << x << " ";

    int winningCounter = 0;
    for (int i = 0; i < yourNumbersLength; i++) {
      for (int j = 0; j < winningNumbersLength; j++) {
        if (yourNumbers[i] == winningNumbers[j]) {
          winningCounter++;
        }
      }
    }

    int points = 0;
    for (int i = 0; i < winningCounter; i++) {
      points = points * 2;
      if (points < 1 ) {
        points = 1;
      }
    }

    cout << winningCounter << " " << points << endl;

    sum += points;
    
  }
  cout << sum << endl;
}
