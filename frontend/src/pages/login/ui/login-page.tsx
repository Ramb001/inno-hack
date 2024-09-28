import { Button } from "@/shared/ui/button";
import { InputWithLabel } from "@/shared/ui/input";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/shared/ui/tabs";

import { useState } from "react";

import { useNavigate } from "react-router-dom";
import { useLoginMutation, useRegisterMutation } from "../api/login-api";

export const LoginPage = () => {
  const [login, setLogin] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [name, setName] = useState<string>("");

  const [isLogineSuccess, setIsLoginSuccess] = useState<boolean>(true);
  const [isRegisterSuccess, setIsRegisterSuccess] = useState<boolean>(true);

  const navigate = useNavigate();

  const [userLogin] = useLoginMutation();
  const [userRegister] = useRegisterMutation();

  function signIn() {
    userLogin({
      username: login,
      password: password,
    })
      .unwrap()
      .then((data) => {
        if (data.status === "success") navigate("/main");
        else setIsLoginSuccess(false);
      });
  }

  function signUp() {
    if (login && email && password && name)
      userRegister({
        username: login,
        password: password,
        email: email,
        name: name,
      })
        .unwrap()
        .then((data) => {
          if (data.status === "success") navigate("/main");
          else setIsRegisterSuccess(false);
        });
    else setIsRegisterSuccess(false);
  }

  return (
    <div className="min-h-screen  flex justify-center items-center">
      <Tabs
        onValueChange={() => {
          setIsLoginSuccess(true);
          setIsRegisterSuccess(true);
        }}
        defaultValue="sign-in"
        className="w-[400px] ">
        <TabsList className="grid w-full grid-cols-2">
          <TabsTrigger value="sign-in">Войти</TabsTrigger>
          <TabsTrigger value="sign-up">Зарегистрироваться</TabsTrigger>
        </TabsList>
        <TabsContent value="sign-in">
          <div className="flex flex-col justify-center items-center gap-3">
            <InputWithLabel
              value={login}
              onChange={(event) => {
                setLogin(event.target.value);
              }}
              label="Логин"
              labelTag="login"
              placeholder="Login"
            />
            <InputWithLabel
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
              }}
              label="Пароль"
              labelTag="password"
              placeholder="Password"
            />
            <div>{!isLogineSuccess ? "Неверный логин или пароль!" : ""}</div>
            <Button className="w-full" onClick={signIn}>
              Войти
            </Button>
          </div>
        </TabsContent>

        <TabsContent value="sign-up">
          <div className="flex flex-col justify-center items-center gap-3">
            <InputWithLabel
              value={name}
              onChange={(event) => {
                setName(event.target.value);
              }}
              label="Введите ваше Имя"
              labelTag="name"
              placeholder="Имя"
            />
            <InputWithLabel
              value={login}
              onChange={(event) => {
                setLogin(event.target.value);
              }}
              label="Придумайте логин"
              labelTag="login"
              placeholder="Логин"
            />
            <InputWithLabel
              value={email}
              onChange={(event) => {
                setEmail(event.target.value);
              }}
              label="Введите ваш email"
              labelTag="email"
              placeholder="Email"
            />
            <InputWithLabel
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
              }}
              label="Придумайте пароль"
              labelTag="password"
              placeholder="Пароль"
            />
            <div>{!isRegisterSuccess ? "Ошибка регистрации!" : ""}</div>
            <Button className="w-full" onClick={signUp}>
              Зарегистрировавться
            </Button>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
};
