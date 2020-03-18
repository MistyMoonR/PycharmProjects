#算法 续航=电量/1000/电流*60

motor_list =["4216","4110"]

#current=int(input("单个电机的电流")) #current=电流

c=1000 #mah转化ah
t=60
#4126电机
motor = input("什么电机?")
    # if (motor in motor_list):
    #     return True
    # else:
    #     return False

result = login()
if(result):#4216
    power = int(input("多少mah?"))
    weight=int(input("整机多重?"))
    axis= int(input("几轴的?"))
    prop = int(input("多大桨？"))
    motor = int(input("再确认一下是什么电机"))

    if motor == 4216:
        voltages = int(input("电池几S？"))
        if voltages == 6:
            if prop==17:
                half_thrust = int(1256)
                half_current = int(4.8)
                if weight > half_thrust*axis:
                    a_weight = (weight - half_thrust*axis) / axis  # 单电机拉力和电流换算
                    current = (half_current + (a_weight * (19.8 / 2359))) * axis  # 总电流计算
                    time = power / c / current * t
                    if time < 5:
                        print("理论续航时间是：", time, "根本飞不起来")
                    else:
                        print("理论续航时间是：", time)
                else:
                    current = half_current * axis
                    print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
            if prop==18:
                half_thrust = int(1501)
                half_current = int(6.1)
                if weight > half_thrust * axis:
                    a_weight = (weight - half_thrust * axis) / axis  # 单电机拉力和电流换算
                    current = (half_current + (a_weight * (24.1 / 1960))) * axis  # 总电流计算
                    time = power / c / current * t
                    if time < 5:
                        print("理论续航时间是：", time, "根本飞不起来")
                    else:
                        print("理论续航时间是：", time)
                else:
                    current = half_current * axis
                    print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)

            else:
                print("桨叶不符合标准或者输入错误")
        else:
            print("你可拉到吧，4216只能用6s")
    if motor == 4110:
        voltages = int(input("电池几S？"))
        if voltages == 6:

            KV_list=["340","400","460"]
            KV = int(input("KV值？"))

            def login():
                global KV
                if (KV in KV_list):
                    return True
                else:
                    counter = 1
                    while (counter < 99):
                        KV = input("KV输入错了吧，在重新输入一遍,这是你第{}边重新输入了。 ".format(counter))
                        if (KV in KV_list):
                            return True
                        counter += 1
                    return False


            result = login()
            if(result):
                KV = int(input("KV值？"))
                if KV == 340:
                    if prop == 15:
                        half_thrust = int(320)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis  # 单电机拉力和电流换算
                            current = (half_current + (a_weight * (12.7 / 1710))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)

                    if prop == 17:
                        half_thrust = int(340)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (17 / 2200))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                if KV == 400:
                    if prop == 12:
                        half_thrust = int(250)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (17 / 1830))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 14:
                        half_thrust = int(290)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (22.3 / 2310))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 15:
                        half_thrust = int(300)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis  # 单电机拉力和电流换算
                            current = (half_current + (a_weight * (22.5 / 2450))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                if KV == 460:
                    if prop == 12:
                        half_thrust = int(250)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (22.8 / 2170))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 14:
                        half_thrust = int(280)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (29 / 2640))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 15:
                        half_thrust = int(280)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust *   axis) / axis  # 单电机拉力和电流换算
                            current = (half_current + (a_weight * (32.9 / 2890))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                if KV == 580:
                    if prop == 12:
                        half_thrust = int(190)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (21.6 / 1600))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 14:
                        half_thrust = int(200)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis
                            current = (half_current + (a_weight * (28.1 / 2050))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                    if prop == 15:
                        half_thrust = int(210)
                        half_current = int(1)
                        if weight > half_thrust * axis:
                            a_weight = (weight - half_thrust * axis) / axis  # 单电机拉力和电流换算
                            current = (half_current + (a_weight * (28.9 / 2190))) * axis  # 总电流计算
                            time = power / c / current * t
                            if time < 5:
                                print("理论续航时间是：", time, "根本飞不起来")
                            else:
                                print("理论续航时间是：", time)
                        else:
                            current = half_current * axis
                            print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
        if voltages == 4:
            if KV == 680:
                if prop == 12:
                    half_thrust = int(180)
                    half_current = int(1)
                    if weight > half_thrust * axis:
                        a_weight = (weight - half_thrust * axis) / axis
                        current = (half_current + (a_weight * (31.6 / 1980))) * axis  # 总电流计算
                        time = power / c / current * t
                        if time < 5:
                            print("理论续航时间是：", time, "根本飞不起来")
                        else:
                            print("理论续航时间是：", time)
                    else:
                        current = half_current * axis
                        print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                if prop == 14:
                    half_thrust = int(190)
                    half_current = int(1)
                    if weight > half_thrust * axis:
                        a_weight = (weight - half_thrust * axis) / axis
                        current = (half_current + (a_weight * (38.6 / 2360))) * axis  # 总电流计算
                        time = power / c / current * t
                        if time < 5:
                            print("理论续航时间是：", time, "根本飞不起来")
                        else:
                            print("理论续航时间是：", time)
                    else:
                        current = half_current * axis
                        print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
                if prop == 15:
                    half_thrust = int(200)
                    half_current = int(1)
                    if weight > half_thrust * axis:
                        a_weight = (weight - half_thrust * axis) / axis  # 单电机拉力和电流换算
                        current = (half_current + (a_weight * (40 /2520))) * axis  # 总电流计算
                        time = power / c / current * t
                        if time< 5:
                            print("理论续航时间是：", time,"根本飞不起来")
                        else:
                            print("理论续航时间是：", time)
                    else:
                        current = half_current * axis
                        print("拉力低于50%油门按50%油门来算，理论续航时间是:", power / c / current * t)
       # else:
            #print("不符合标准或者输入错误")
        #if voltages ==


        else:
            print("你可拉到吧，4110只能用6s或者4S")
    else:
        print("傻逼，电机输错了吧")
else:
    print("很抱歉数据库没有这个破电机,目前只支持",motor_list,"哦")

#d=b*4
#print("理论续航时间",c/d*60)

