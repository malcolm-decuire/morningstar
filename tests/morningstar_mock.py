from morningstar.provider.morningstar import Morningstar


class MorningstarMock(Morningstar):

    def __init__(self):
        super().__init__({})

    def search(self, params):
        return [{'Symbol': 'JPM', 'Exchange': '50', 'Security Type': '1'},
                {'Symbol': '8634/N', 'Exchange': '109', 'Security Type': '1'},
                {'Symbol': 'CMC/D', 'Exchange': '109', 'Security Type': '1'},
                {'Symbol': 'JPM/N', 'Exchange': '109', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '1', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '2', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '3', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '8', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '9', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '12', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '13', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '14', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '15', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '16', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '17', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '19', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '20', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '23', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '24', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '26', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '126', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '131', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '149', 'Security Type': '1'},
                {'Symbol': '0Q1F', 'Exchange': '151', 'Security Type': '1'},
                {'Symbol': '0Q1F', 'Exchange': '152', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '157', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '163', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '182', 'Security Type': '1'},
                {'Symbol': 'JPM/US', 'Exchange': '182', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '194', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '200', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '213', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '214', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '216', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '218', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '219', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '220', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '215', 'Security Type': '1'},
                {'Symbol': 'CMC/O', 'Exchange': '215', 'Security Type': '1'},
                {'Symbol': 'CMC', 'Exchange': '217', 'Security Type': '1'},
                {'Symbol': 'M-US46625H1005', 'Exchange': '223', 'Security Type': '1'},
                {'Symbol': 'JPM/N', 'Exchange': '226', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '228', 'Security Type': '1'},
                {'Symbol': 'JPM', 'Exchange': '233', 'Security Type': '1'}]

    def index(self, params):
        pass

    def index_ts(self, params):
        return {
            'symbol': 'USDCHFLITE', 'exchangeid': '245', 'type': '20', 'data': [
                {'Date Received (GMT)': '06-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98625', 'High price': '0.987', 'Low price': '0.9851', 'Last price': '0.98576'},
                {'Date Received (GMT)': '05-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98625', 'High price': '0.98625', 'Low price': '0.98625', 'Last price': '0.98625'},
                {'Date Received (GMT)': '04-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98726', 'High price': '0.99068', 'Low price': '0.9852', 'Last price': '0.98625'},
                {'Date Received (GMT)': '03-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98916', 'High price': '0.98977', 'Low price': '0.9845', 'Last price': '0.9871'},
                {'Date Received (GMT)': '02-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9818', 'High price': '0.99176', 'Low price': '0.9794', 'Last price': '0.9887'},
                {'Date Received (GMT)': '01-01-2019', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98351', 'High price': '0.9839', 'Low price': '0.9806', 'Last price': '0.982'},
                {'Date Received (GMT)': '31-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98371', 'High price': '0.9873', 'Low price': '0.9809', 'Last price': '0.98351'},
                {'Date Received (GMT)': '30-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98403', 'High price': '0.9846', 'Low price': '0.9833', 'Last price': '0.9836'},
                {'Date Received (GMT)': '29-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98403', 'High price': '0.9841', 'Low price': '0.98403', 'Last price': '0.98403'},
                {'Date Received (GMT)': '28-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9871', 'High price': '0.9871', 'Low price': '0.9791', 'Last price': '0.98403'},
                {'Date Received (GMT)': '27-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99441', 'High price': '0.99451', 'Low price': '0.98455', 'Last price': '0.9869'},
                {'Date Received (GMT)': '26-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9864', 'High price': '0.99622', 'Low price': '0.9855', 'Last price': '0.9943'},
                {'Date Received (GMT)': '25-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9862', 'High price': '0.9886', 'Low price': '0.9799', 'Last price': '0.9861'},
                {'Date Received (GMT)': '24-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9937', 'High price': '0.9951', 'Low price': '0.98498', 'Last price': '0.9858'},
                {'Date Received (GMT)': '23-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99321', 'High price': '0.9952', 'Low price': '0.99321', 'Last price': '0.9936'},
                {'Date Received (GMT)': '22-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99486', 'High price': '0.99486', 'Low price': '0.99321', 'Last price': '0.99321'},
                {'Date Received (GMT)': '21-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98696', 'High price': '0.99561', 'Low price': '0.986', 'Last price': '0.99486'},
                {'Date Received (GMT)': '20-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99394', 'High price': '0.99517', 'Low price': '0.98408', 'Last price': '0.987'},
                {'Date Received (GMT)': '19-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9922', 'High price': '0.99549', 'Low price': '0.9905', 'Last price': '0.9939'},
                {'Date Received (GMT)': '18-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9925', 'High price': '0.99364', 'Low price': '0.98999', 'Last price': '0.9924'},
                {'Date Received (GMT)': '17-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99756', 'High price': '0.99813', 'Low price': '0.9917', 'Last price': '0.99261'},
                {'Date Received (GMT)': '16-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99786', 'High price': '0.99832', 'Low price': '0.99651', 'Last price': '0.99751'},
                {'Date Received (GMT)': '15-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99786', 'High price': '0.99786', 'Low price': '0.99786', 'Last price': '0.99786'},
                {'Date Received (GMT)': '14-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99359', 'High price': '0.9988', 'Low price': '0.9933', 'Last price': '0.99786'},
                {'Date Received (GMT)': '13-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99278', 'High price': '0.99532', 'Low price': '0.9912', 'Last price': '0.9936'},
                {'Date Received (GMT)': '12-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9929', 'High price': '0.9963', 'Low price': '0.9914', 'Last price': '0.9926'},
                {'Date Received (GMT)': '11-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9893', 'High price': '0.99372', 'Low price': '0.9863', 'Last price': '0.99316'},
                {'Date Received (GMT)': '10-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98955', 'High price': '0.99058', 'Low price': '0.9869', 'Last price': '0.9895'},
                {'Date Received (GMT)': '09-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99026', 'High price': '0.99142', 'Low price': '0.9891', 'Last price': '0.98972'},
                {'Date Received (GMT)': '08-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99026', 'High price': '0.99026', 'Low price': '0.99026', 'Last price': '0.99026'},
                {'Date Received (GMT)': '07-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99313', 'High price': '0.99429', 'Low price': '0.98905', 'Last price': '0.99026'},
                {'Date Received (GMT)': '06-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99707', 'High price': '0.99896', 'Low price': '0.98955', 'Last price': '0.9932'},
                {'Date Received (GMT)': '05-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99738', 'High price': '1.00066', 'Low price': '0.9966', 'Last price': '0.99702'},
                {'Date Received (GMT)': '04-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.998', 'High price': '0.99887', 'Low price': '0.993', 'Last price': '0.9972'},
                {'Date Received (GMT)': '03-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99858', 'High price': '0.99948', 'Low price': '0.9964', 'Last price': '0.99782'},
                {'Date Received (GMT)': '02-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99886', 'High price': '0.9995', 'Low price': '0.9973', 'Last price': '0.9983'},
                {'Date Received (GMT)': '01-12-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99812', 'High price': '0.99886', 'Low price': '0.99812', 'Last price': '0.99886'},
                {'Date Received (GMT)': '30-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99601', 'High price': '1.00021', 'Low price': '0.995', 'Last price': '0.99812'},
                {'Date Received (GMT)': '29-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9933', 'High price': '0.99755', 'Low price': '0.9916', 'Last price': '0.9959'},
                {'Date Received (GMT)': '28-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9982', 'High price': '1.0005', 'Low price': '0.9924', 'Last price': '0.993'},
                {'Date Received (GMT)': '27-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9982', 'High price': '1.00022', 'Low price': '0.9973', 'Last price': '0.9982'},
                {'Date Received (GMT)': '26-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99727', 'High price': '0.99926', 'Low price': '0.9953', 'Last price': '0.99822'},
                {'Date Received (GMT)': '25-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99692', 'High price': '0.99738', 'Low price': '0.9964', 'Last price': '0.99732'},
                {'Date Received (GMT)': '24-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99696', 'High price': '0.99696', 'Low price': '0.99692', 'Last price': '0.99692'},
                {'Date Received (GMT)': '23-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9943', 'High price': '0.99793', 'Low price': '0.9933', 'Last price': '0.99696'},
                {'Date Received (GMT)': '22-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9941', 'High price': '0.99555', 'Low price': '0.99226', 'Last price': '0.9943'},
                {'Date Received (GMT)': '21-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99471', 'High price': '0.99582', 'Low price': '0.99275', 'Last price': '0.9941'},
                {'Date Received (GMT)': '20-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99313', 'High price': '0.99562', 'Low price': '0.9908', 'Last price': '0.99472'},
                {'Date Received (GMT)': '19-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99947', 'High price': '1.00065', 'Low price': '0.9922', 'Last price': '0.993'},
                {'Date Received (GMT)': '18-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99786', 'High price': '1.0005', 'Low price': '0.99786', 'Last price': '0.99938'},
                {'Date Received (GMT)': '17-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99969', 'High price': '0.99969', 'Low price': '0.99786', 'Last price': '0.99786'},
                {'Date Received (GMT)': '16-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00692', 'High price': '1.00856', 'Low price': '0.9989', 'Last price': '0.99969'},
                {'Date Received (GMT)': '15-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00597', 'High price': '1.00764', 'Low price': '1.0036', 'Last price': '1.0067'},
                {'Date Received (GMT)': '14-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00584', 'High price': '1.01031', 'Low price': '1.0041', 'Last price': '1.0059'},
                {'Date Received (GMT)': '13-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0103', 'High price': '1.01268', 'Low price': '1.0056', 'Last price': '1.0058'},
                {'Date Received (GMT)': '12-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0056', 'High price': '1.01106', 'Low price': '1.0054', 'Last price': '1.01021'},
                {'Date Received (GMT)': '11-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0052', 'High price': '1.0062', 'Low price': '1.005', 'Last price': '1.0059'},
                {'Date Received (GMT)': '10-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0052', 'High price': '1.0052', 'Low price': '1.0052', 'Last price': '1.0052'},
                {'Date Received (GMT)': '09-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0057', 'High price': '1.0084', 'Low price': '1.00446', 'Last price': '1.0052'},
                {'Date Received (GMT)': '08-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0016', 'High price': '1.00703', 'Low price': '1.0007', 'Last price': '1.0056'},
                {'Date Received (GMT)': '07-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00131', 'High price': '1.00488', 'Low price': '0.995', 'Last price': '1.0018'},
                {'Date Received (GMT)': '06-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0044', 'High price': '1.00548', 'Low price': '1.0014', 'Last price': '1.00158'},
                {'Date Received (GMT)': '05-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00253', 'High price': '1.00674', 'Low price': '1.0025', 'Last price': '1.0042'},
                {'Date Received (GMT)': '04-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0016', 'High price': '1.0029', 'Low price': '1.0016', 'Last price': '1.0024'},
                {'Date Received (GMT)': '03-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0016', 'High price': '1.0016', 'Low price': '1.0016', 'Last price': '1.0016'},
                {'Date Received (GMT)': '02-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.0019', 'High price': '1.00477', 'Low price': '0.9968', 'Last price': '1.0016'},
                {'Date Received (GMT)': '01-11-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00821', 'High price': '1.00821', 'Low price': '1.00032', 'Last price': '1.002'},
                {'Date Received (GMT)': '31-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00517', 'High price': '1.00944', 'Low price': '1.0032', 'Last price': '1.00795'},
                {'Date Received (GMT)': '30-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '1.00172', 'High price': '1.00541', 'Low price': '1.0006', 'Last price': '1.005'},
                {'Date Received (GMT)': '29-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9974', 'High price': '1.00236', 'Low price': '0.9974', 'Last price': '1.00173'},
                {'Date Received (GMT)': '28-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99681', 'High price': '0.99783', 'Low price': '0.9965', 'Last price': '0.9974'},
                {'Date Received (GMT)': '27-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99681', 'High price': '0.99681', 'Low price': '0.99681', 'Last price': '0.99681'},
                {'Date Received (GMT)': '26-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99957', 'High price': '1.00259', 'Low price': '0.9963', 'Last price': '0.99681'},
                {'Date Received (GMT)': '25-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.997', 'High price': '1.00159', 'Low price': '0.9954', 'Last price': '0.99967'},
                {'Date Received (GMT)': '24-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99477', 'High price': '0.9988', 'Low price': '0.99421', 'Last price': '0.99687'},
                {'Date Received (GMT)': '23-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.996', 'High price': '0.99688', 'Low price': '0.9938', 'Last price': '0.99466'},
                {'Date Received (GMT)': '22-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9961', 'High price': '0.99794', 'Low price': '0.99405', 'Last price': '0.99611'},
                {'Date Received (GMT)': '21-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99572', 'High price': '0.99664', 'Low price': '0.9956', 'Last price': '0.9962'},
                {'Date Received (GMT)': '20-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99572', 'High price': '0.99572', 'Low price': '0.99572', 'Last price': '0.99572'},
                {'Date Received (GMT)': '19-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99582', 'High price': '0.9977', 'Low price': '0.99491', 'Last price': '0.99572'},
                {'Date Received (GMT)': '18-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99479', 'High price': '0.99744', 'Low price': '0.9919', 'Last price': '0.99573'},
                {'Date Received (GMT)': '17-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9904', 'High price': '0.99557', 'Low price': '0.99', 'Last price': '0.99505'},
                {'Date Received (GMT)': '16-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9868', 'High price': '0.99076', 'Low price': '0.98596', 'Last price': '0.99042'},
                {'Date Received (GMT)': '15-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99079', 'High price': '0.99111', 'Low price': '0.98486', 'Last price': '0.98703'},
                {'Date Received (GMT)': '14-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99171', 'High price': '0.99196', 'Low price': '0.98955', 'Last price': '0.9907'},
                {'Date Received (GMT)': '13-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99171', 'High price': '0.99171', 'Low price': '0.99171', 'Last price': '0.99171'},
                {'Date Received (GMT)': '12-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98998', 'High price': '0.9929', 'Low price': '0.9883', 'Last price': '0.99171'},
                {'Date Received (GMT)': '11-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98842', 'High price': '0.9921', 'Low price': '0.98567', 'Last price': '0.9898'},
                {'Date Received (GMT)': '10-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99173', 'High price': '0.99331', 'Low price': '0.98794', 'Last price': '0.98823'},
                {'Date Received (GMT)': '09-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.992', 'High price': '0.99553', 'Low price': '0.99081', 'Last price': '0.9916'},
                {'Date Received (GMT)': '08-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9914', 'High price': '0.99433', 'Low price': '0.9906', 'Last price': '0.9921'},
                {'Date Received (GMT)': '07-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99143', 'High price': '0.99238', 'Low price': '0.9912', 'Last price': '0.99141'},
                {'Date Received (GMT)': '06-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.99169', 'High price': '0.99169', 'Low price': '0.99143', 'Last price': '0.99143'},
                {'Date Received (GMT)': '05-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9914', 'High price': '0.9949', 'Low price': '0.99102', 'Last price': '0.99169'},
                {'Date Received (GMT)': '04-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9917', 'High price': '0.9932', 'Low price': '0.98982', 'Last price': '0.99135'},
                {'Date Received (GMT)': '03-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.9838', 'High price': '0.99234', 'Low price': '0.9833', 'Last price': '0.99175'},
                {'Date Received (GMT)': '02-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98361', 'High price': '0.98626', 'Low price': '0.9828', 'Last price': '0.98377'},
                {'Date Received (GMT)': '01-10-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98139', 'High price': '0.98539', 'Low price': '0.9805', 'Last price': '0.9834'},
                {'Date Received (GMT)': '30-09-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98173', 'High price': '0.98173', 'Low price': '0.97969', 'Last price': '0.9812'},
                {'Date Received (GMT)': '29-09-2018', 'Time Received (GMT)': '00:00', 'Cumulative volume': '0',
                 'Open price': '0.98173', 'High price': '0.98173', 'Low price': '0.98173', 'Last price': '0.98173'}
            ]
        }
