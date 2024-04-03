class TrafficLight:
    '''
    class of traffic light

    parameters:
    current_signal - current signal of traffic light
    permissible_values - all possible signals
    previous - previous signal
    '''

    def __init__(self):
        self.current_signal = 'зелёный'
        self.permissible_values = ['зелёный','жёлтый','красный']
        self.previous = 'зелёный'

    def next_signal(self):
        '''
        function turns current signsr to next
        '''

        if self.current_signal == 'зелёный':
            self.current_signal = 'жёлтый'
            self.previous = 'зелёный'
            return
        if self.current_signal == 'красный':
            self.current_signal = 'жёлтый'
            self.previous = 'красный'
            return
        if self.current_signal == 'жёлтый':
            if self.previous == 'зелёный':
                self.current_signal = 'красный'
                self.previous = 'желтый'
                return
            else:
                self.current_signal = 'зелёный'
                self.previous = 'желтый'
                return

light1 = TrafficLight()


light1.next_signal()

light1.next_signal()

light1.next_signal()

light1.next_signal()



print(light1.current_signal)
