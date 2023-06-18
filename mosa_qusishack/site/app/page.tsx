import Head from "next/head";
import Image from "next/image";
import QusisHack from "../components/qusishack";

export default function Home() {
  return (
    <>
      <Head>
        <title>Qusis Hack</title>
        <meta
          name="description"
          content="Give you a hint to be a better developer"
        />
        <link rel="svg" href="/next.svg"/>
      </Head>
      <QusisHack/>
    </>
  );
}