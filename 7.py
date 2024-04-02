doc = []

class TrafficLight:
    '''
    class of traffic light

    parameters:
    current_signal - current signal of traffic light
    '''

    def __init__(self):
        self.current_signal = 'зелёный'

    def next_signal(self, doc):
        '''
        function turns current signsr to next

        :param doc: log file with all previous signals
        '''

        if self.current_signal == 'зелёный':
            self.current_signal = 'жёлтый'
            doc.append('зелёный')
            return
        if self.current_signal == 'красный':
            self.current_signal = 'жёлтый'
            doc.append('красный')
            return
        if self.current_signal == 'жёлтый':
            if doc[-1] == 'зелёный':
                self.current_signal = 'красный'
                doc.append('желтый')
                return
            else:
                self.current_signal = 'зелёный'
                doc.append('желтый')
                return

light1 = TrafficLight()


light1.next_signal(doc)

light1.next_signal(doc)

light1.next_signal(doc)

light1.next_signal(doc)



print(light1.current_signal)