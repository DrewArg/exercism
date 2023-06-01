export function hey(message: string): string {
  let response: string;

  let yellQuestion = new RegExp(/[A-Z\s]+\?$/g);
  let question = new RegExp(/\?$/g);
  let noLowerCase = new RegExp(/[^a-z]+[A-Z]+/g);
  let spaces = new RegExp(/[\t\n\r]+/g);

  if (yellQuestion.test(message)) {
    response = "Calm down, I know what I'm doing!";
  } else if (question.test(message)) {
    response = "Sure.";
  } else if (noLowerCase.test(message)) {
    response = "Whoa, chill out!";
  } else if (spaces.test(message)) {
    response = "Fine. Be that way!";
  } else {
    response = "Whatever.";
  }

  return response;
}
