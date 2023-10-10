import re
import random
import unicodedata

class ChatBot:
    def __init__(self, responses):
        self.highest_prob = {}
        self.responses = responses

    def get_response(self, user_input):
        normalized_message = unicodedata.normalize('NFKD', user_input).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        split_message = re.split(r'\s|[,:;.?!-_]\s*', normalized_message.lower())
        response = self.check_all_messages(split_message)
        return response

    def message_probability(self, user_message, recognized_words, single_response=False, required_words=[]):
        message_certainty = sum([1 for word in user_message if word in recognized_words])
        percentage = float(message_certainty) / float(len(recognized_words))
        has_required_words = all([word in user_message for word in required_words])
        if has_required_words or single_response:
            return int(percentage * 100)
        else:
            return 0

    def check_all_messages(self, message):
        for response in self.responses:
            self.response(message, response['bot_response'], response['list_of_words'], response.get('single_response', False), response.get('required_words', []))

        best_match = max(self.highest_prob, key=self.highest_prob.get)
        return self.unknown() if self.highest_prob[best_match] < 1 else best_match

    def response(self, message, bot_response, list_of_words, single_response=False, required_words=[]):
        self.highest_prob[bot_response] = self.message_probability(message, list_of_words, single_response, required_words)

    def unknown(self):
        response = random.choice(['No estoy seguro de lo que quieres.', '¿Podrías escribirlo de otro modo?', 'Te sugiero escribirnos al correo info@itla.edu.do'])
        return response
