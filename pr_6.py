def normal_kkal(years_old, weight, height, gender):
    '''Сalculation of optimal calorie intake'''
    if gender == 'ж':
        BMR = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * years_old)
        return BMR
    if gender=='м':
        BMR = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * years_old)
        return BMR

def coefficient(activity):
    '''Сalculation of basal metabolism'''
    if activity == 'минимальный':
        AMR = 1.2
        return AMR
    if activity == 'низкий':
        AMR = 1.375
        return AMR
    if activity == 'средний':
        AMR = 1.55
        return AMR
    if activity == 'высокий':
        AMR = 1.725
        return AMR
    if activity == 'очень высокий':
        AMR = 1.9
        return AMR

def weight_maintenance(years_old, weight, height, gender, activity):
    '''Calculating calories for weight maintenance'''
    kkal = round(normal_kkal(years_old, weight, height, gender) * coefficient(activity))
    proteins = round((kkal * 0.35) / 4, 1)
    fats = round((kkal * 0.25) / 9, 1)
    carbohydrates = round((kkal * 0.6) / 4, 1)
    print('Для поддержания веса вам необходимо потреблять {} ккал.'.format(kkal))
    print('Рекомендуемая норма потребления {} гр. белков, {} гр. жиров, {} гр. углеводов.'
          .format(proteins, fats, carbohydrates))

def weight_loss(years_old, weight, height, gender, activity):
    '''Calculating calories for weight loss'''
    AMR = 0.8
    kkal = round(normal_kkal(years_old, weight, height, gender) * AMR)
    proteins = round((kkal * 0.35) / 4, 1)
    fats = round((kkal * 0.25) / 9, 1)
    carbohydrates = round((kkal * 0.6) / 4, 1)
    print('Для похудения вам необходима потреблять {}'.format(kkal))
    print('Рекомендуемая норма потребления {} гр. белков, {} гр. жиров, {} гр. углеводов.'
          .format(proteins, fats, carbohydrates))

def weight_gain(years_old, weight, height, gender, activity):
    '''Calculating calories for weight gain'''
    AMR = 1.2
    kkal = round(normal_kkal(years_old, weight, height, gender) * AMR)
    proteins = round((kkal * 0.35) / 4, 1)
    fats = round((kkal * 0.25) / 9, 1)
    carbohydrates = round((kkal * 0.6) / 4, 1)
    print('Для набора веса вам необходима потреблять {}'.format(kkal))
    print('Рекомендуемая норма потребления {} гр. белков, {} гр. жиров, {} гр. углеводов.'
          .format(proteins, fats, carbohydrates))

def main():
    '''Main function'''
    print('Привет, дорогой пользователь! Введи, пожалуйста, следующие данные.')
    gender = input('Ваш пол (указать м или ж): ')
    years_old = int(input('Ваш возраст (полных лет): '))
    weight = int(input('Ваш вес (в кг): '))
    height = int(input('Ваш рост (в см): '))
    activity = input('Напишите ваш уровень физичсеких нагрузок '
                     '(минимальный/низкий/средний/высокий/очень высокий): ')
    print('Если ваша цель поддержать вес, нажмите 1')
    print('Если ваша цель похудеть, нажмите 2')
    print('Если ваша цель набрать мышечную массу, нажмите 3')
    goal = int(input('Ваша цель: '))
    if goal == 1:
        weight_maintenance(years_old, weight, height, gender, activity)
    elif goal == 2:
        weight_loss(years_old, weight, height, gender, activity)
    elif goal == 3:
        weight_gain(years_old, weight, height, gender, activity)

if __name__=='__main__':
    main()
