import { Button } from "@/shared/ui/button";
import { InputWithLabel } from "@/shared/ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/shared/ui/tabs";

import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";
import { useLoginMutation, useRegisterMutation } from "../api/login-api";

export const LoginPage = () => {
  const [login, setLogin] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [name, setName] = useState<string>("");

  const [loginMarking, setLoginMarking] = useState<boolean>(false);
  const [emailMarking, setEmailMarking] = useState<boolean>(false);
  const [passwordMarking, setPasswordMarking] = useState<boolean>(false);
  const [nameMarking, setNameMarking] = useState<boolean>(false);

  const [isLogineSuccess, setIsLoginSuccess] = useState<boolean>(true);
  const [isRegisterSuccess, setIsRegisterSuccess] = useState<boolean>(true);

  const navigate = useNavigate();

  const [userLogin] = useLoginMutation();
  const [userRegister] = useRegisterMutation();

  useEffect(() => {
    if (sessionStorage.getItem("userId")) navigate("/main");
  });

  function signIn() {
    if (!login) setLoginMarking(true);
    if (!password) setPasswordMarking(true);
    if (login && password)
      userLogin({
        username: login,
        password: password,
      })
        .unwrap()
        .then((data) => {
          console.log(data);
          if (data.status === "success") {
            navigate("/main");
            sessionStorage.setItem("userId", data.user_id);
            sessionStorage.setItem("userEmail", data.email);
            sessionStorage.setItem("userName", data.name);
            sessionStorage.setItem("userLogin", data.username);
          } else setIsLoginSuccess(false);
        });
  }

  function signUp() {
    if (!login) setLoginMarking(true);
    if (!email) setEmailMarking(true);
    if (!password) setPasswordMarking(true);
    if (!name) setNameMarking(true);

    if (login && email && password && name)
      userRegister({
        username: login,
        password: password,
        email: email,
        name: name,
      })
        .unwrap()
        .then((data) => {
          if (data.status === "success") signIn();
          else setIsRegisterSuccess(false);
        });
  }

  return (
    <div className="min-h-screen  flex justify-center items-center">
      <Tabs
        onValueChange={() => {
          setIsLoginSuccess(true);
          setIsRegisterSuccess(true);

          setLogin("");
          setEmail("");
          setPassword("");
          setName("");

          setLoginMarking(false);
          setEmailMarking(false);
          setPasswordMarking(false);
          setNameMarking(false);
        }}
        defaultValue="sign-in"
        className="w-[400px] ">
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="sign-in">Войти</TabsTrigger>
          <TabsTrigger value="sign-up">Зарегистрироваться</TabsTrigger>
        </TabsList>
        <TabsContent value="sign-in">
          <div className="flex flex-col justify-center items-center p-3 gap-3">
            <InputWithLabel
              value={login}
              className={`${loginMarking && "bg-marking"}`}
              onChange={(event) => {
                setLoginMarking(false);
                setLogin(event.target.value);
              }}
              label="Логин"
              labelTag="login"
              placeholder="Логин"
            />
            <InputWithLabel
              value={password}
              className={`${passwordMarking && "bg-marking"}`}
              onChange={(event) => {
                setPasswordMarking(false);
                setPassword(event.target.value);
              }}
              label="Пароль"
              labelTag="password"
              placeholder="Пароль"
            />
            <div className="h-4 text-xs text-[#8a0000]">
              {!isLogineSuccess ? "Неверный логин или пароль!" : ""}
            </div>
            <Button className="w-full" onClick={signIn}>
              Войти
            </Button>
          </div>
        </TabsContent>

        <TabsContent value="sign-up">
          <div className="flex flex-col justify-center items-center p-3 gap-3">
            <InputWithLabel
              value={name}
              className={`${nameMarking && "bg-marking"}`}
              onChange={(event) => {
                setNameMarking(false);
                setName(event.target.value);
              }}
              label="Введите ваше Имя"
              labelTag="name"
              placeholder="Имя"
            />
            <InputWithLabel
              value={login}
              className={`${loginMarking && "bg-marking"}`}
              onChange={(event) => {
                setLoginMarking(false);
                setLogin(event.target.value);
              }}
              label="Придумайте логин"
              labelTag="login"
              placeholder="Логин"
            />
            <InputWithLabel
              value={email}
              className={`${emailMarking && "bg-marking"}`}
              onChange={(event) => {
                setEmailMarking(false);
                setEmail(event.target.value);
              }}
              label="Введите ваш email"
              labelTag="email"
              placeholder="Email"
            />
            <InputWithLabel
              value={password}
              className={`${passwordMarking && "bg-marking"}`}
              onChange={(event) => {
                setPasswordMarking(false);
                setPassword(event.target.value);
              }}
              label="Придумайте пароль"
              labelTag="password"
              placeholder="Пароль"
            />
            <div className="h-4 text-xs text-[#8a0000]">
              {!isRegisterSuccess ? "Ошибка регистрации!" : ""}
            </div>
            <Button className="w-full" onClick={signUp}>
              Зарегистрировавться
            </Button>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
};
