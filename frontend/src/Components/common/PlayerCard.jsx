import React from "react";
import styled from "styled-components";

function PlayerCard(props) {
  return (
    <Wrapper>
      <BestCardContainer>
        <Image src={props.image} />
        <Title>{props.title}</Title>
      </BestCardContainer>
    </Wrapper>
  );
}

export default PlayerCard;

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 30vh;
`;

const BestCardContainer = styled.div`
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 90%;
  height: 91%;
  border-radius: 20px;
  box-shadow: 5px 5px 15px 1px black;
  overflow: hidden;
  &:hover {
    transform: scale(1.05);
    transition: transform 0.8s;
  }
`;

const Image = styled.img`
  width: 100%;
  height: 100%;
  border-radius: 20px;
  object-fit: cover !important;
`;

const Title = styled.div`
  display: flex;
  background: linear-gradient(to bottom, rgba(1, 0, 0, 0), rgba(1, 1, 1, 0.8));
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 30%;
  font-size: 30px;
  font-family: "KOTRAHOPE";
  font-weight: normal;
  font-style: normal;
  color: ${(props) => props.theme.colors.white};
  text-align: center;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
  position: absolute;
  bottom: 0px;
`;